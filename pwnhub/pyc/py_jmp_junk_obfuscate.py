import marshal
import random
import dis
import types

has_args = [131, 147, 120, 104, 145, 122, 141, 121, 90, 108, 116, 101, 93, 91, 103, 107, 125, 140, 146, 119, 98, 135, 95,
            105, 143, 92, 94, 97, 132, 99, 142, 106, 109, 126, 100, 137, 102, 96, 115, 111, 130, 114, 136, 124, 112, 133, 113, 134, 110]
no_args = [4, 28, 65, 88, 83, 87, 1, 29, 77, 85, 66, 57, 82, 70, 68, 0, 12, 62, 84, 79, 24, 54, 55, 75, 59, 21, 76, 73, 20, 74, 9, 78, 56, 67,
           5, 61, 64, 80, 51, 50, 27, 2, 23, 11, 10, 60, 19, 89, 13, 22, 53, 52, 81, 71, 30, 31, 32, 33, 26, 63, 25, 86, 3, 40, 41, 42, 43, 15, 72, 58]
all_code = has_args + no_args


def n2b(n):
    return chr(n & 0xff) + chr((n / 0x100) & 0xff)


def b2n(b):
    return ord(b[0]) + ord(b[1]) * 0x100


def find_jmp(code_block):
    code = code_block[0]
    code_range = code_block[1]
    i = 0
    jmp_addr_dict = {}
    while(i < len(code)):
        c = ord(code[i])
        if c in has_args:
            if c in dis.hasjabs or c in dis.hasjrel:
                if c in dis.hasjabs:
                    target_addr = b2n(code[i + 1:i + 3])
                else:
                    delta = b2n(code[i + 1:i + 3])
                    target_addr = code_range[0] + i + 3 + delta
                jmp_addr_dict[i] = target_addr
            i += 3
        else:
            i += 1
    return jmp_addr_dict


def patch_code(code_blocks, jmp_addr_dict, code_block_id, next_code_block_id, code_block_new_position_dict):
    code = code_blocks[code_block_id][0]
    code_range = code_blocks[code_block_id][1]
    code_block_position = code_block_new_position_dict[code_block_id]
    new_code = ''
    i = 0
    count = 0
    p = []
    while(i < len(code)):
        c = ord(code[i])
        if i in jmp_addr_dict:
            p += [i]
            delta = len(code) + 3 - i - 3 + count * 3
            new_code += code[i]
            if c in dis.hasjabs:
                target_addr = delta + i + 3 + code_block_position
                new_code += n2b(target_addr)
            elif c in dis.hasjrel:
                new_code += n2b(delta)
            count += 1
            i += 3
        else:
            if c in no_args:
                new_code += code[i]
                i += 1
            else:
                new_code += code[i:i + 3]
                i += 3

    next_position = code_block_position + len(new_code) + 3
    if next_code_block_id:
        next_code_block_position = code_block_new_position_dict[
            next_code_block_id]
    else:
        next_code_block_position = next_position - 3
    if next_code_block_position >= next_position:
        delta = next_code_block_position - next_position
        new_code += chr(dis.opmap['JUMP_FORWARD']) + n2b(delta)
    else:
        new_code += chr(dis.opmap['JUMP_ABSOLUTE']) + \
            n2b(next_code_block_position)

    for i in p:
        target_addr = jmp_addr_dict[i]
        next_position += 3
        for code_block_id in code_blocks:
            if target_addr in code_blocks[code_block_id][1]:
                new_target_addr = target_addr - \
                    code_blocks[code_block_id][1][0] + \
                    code_block_new_position_dict[code_block_id]
                if new_target_addr >= next_position:
                    delta = new_target_addr - next_position
                    new_code += chr(dis.opmap['JUMP_FORWARD']) + n2b(delta)
                else:
                    new_code += chr(dis.opmap['JUMP_ABSOLUTE']
                                    ) + n2b(new_target_addr)
    return new_code


def add_junk_code(junk_size):
    code = ''
    # code += '\x09'*junk_size
    for i in xrange(junk_size):
        code += chr(random.choice(all_code))
    if ord(code[-1]) in no_args:
        code = code[:-1] + chr(random.choice(has_args))
    return code


def make_code_block(code, obfuscate=False):
    i = 0
    code_block_id_xref_dict = {}
    code_labels = dis.findlabels(code) if obfuscate else []
    code_blocks = {}
    code_block_id_tab = []
    while(i < len(code)):
        code_size = random.randint(
            3, 5) if obfuscate else random.randint(8, 10)
        code_block = ''
        tmp = i
        while(code_size and i < len(code)):
            c = ord(code[i])
            if i in code_labels:
                if not code_block == '':
                    break
            if obfuscate and (c in dis.hasjabs or c in dis.hasjrel):
                code_block += code[i:i + 3]
                i += 3
                break
            elif c in has_args:
                code_block += code[i:i + 3]
                i += 3
            else:
                code_block += code[i]
                i += 1
            code_size -= 1
        code_block_id = random.randint(1, 0xffffffff)
        while code_block_id in code_block_id_tab:
            code_block_id = random.randint(1, 0xffffffff)

        code_block_id_tab += [code_block_id]
        code_blocks[code_block_id] = [code_block, xrange(tmp, i)]

    for i, v in enumerate(code_block_id_tab[:-1]):
        code_block_id_xref_dict[v] = code_block_id_tab[i + 1]

    begin = code_block_id_tab[0]

    return code_blocks, begin, code_block_id_tab, code_block_id_xref_dict


def make_junk_code(code):
    # code_blocks = {block_id:[block_code,block_range]}
    code_blocks, begin, code_block_id_tab, code_block_id_xref_dict = make_code_block(
        code.co_code)
    add_junk_code_dict = {}
    add_jmp_dict = {}
    code_block_new_position_dict = {}

    random.shuffle(code_block_id_tab)

    junk_code_max_size = (0x10000 - len(code.co_code) -
                          len(dis.findlabels(code.co_code))) / len(code_block_id_tab) - 5
    junk_code_max_size = 9 if junk_code_max_size > 9 else junk_code_max_size
    junk_code = add_junk_code(random.randint(
        junk_code_max_size / 2, junk_code_max_size))
    begin_position = 3 + len(junk_code)

    for code_block_id in code_block_id_tab:
        add_junk_code_dict[code_block_id] = add_junk_code(
            random.randint(junk_code_max_size / 2, junk_code_max_size))
        add_jmp_dict[code_block_id] = find_jmp(code_blocks[code_block_id])
        code_block_new_position_dict[code_block_id] = begin_position
        begin_position += len(code_blocks[code_block_id][0]) + 3 + 3 * len(
            add_jmp_dict[code_block_id]) + len(add_junk_code_dict[code_block_id])

    co_code = chr(dis.opmap['JUMP_ABSOLUTE']) + \
        n2b(code_block_new_position_dict[begin]) + junk_code
    for code_block_id in code_block_id_tab:
        next_code_block_id = 0
        if code_block_id in code_block_id_xref_dict:
            next_code_block_id = code_block_id_xref_dict[code_block_id]
        co_code += patch_code(code_blocks, add_jmp_dict[code_block_id], code_block_id,
                              next_code_block_id, code_block_new_position_dict) + add_junk_code_dict[code_block_id]

    co_consts = []
    for v in code.co_consts:
        if isinstance(v, types.CodeType):
            co_consts += [make_junk_code(v)]
        else:
            co_consts += [v]
    co_consts = tuple(co_consts)
    if len(co_code) > 0xffff:
        print '[ERROR]code is too long.'
    return types.CodeType(code.co_argcount, code.co_nlocals, code.co_stacksize, code.co_flags, co_code, co_consts, code.co_names, code.co_varnames, code.co_filename, code.co_name, code.co_firstlineno, code.co_lnotab)


def make_code_obfuscate(code):
    code_blocks, begin, code_block_id_tab, code_block_id_xref_dict = make_code_block(
        code.co_code, True)
    # code_blocks = {block_id:[block_code,block_range]}
    co_varnames = [v for v in code.co_varnames]
    co_varnames += ['DIVIDER']
    co_nlocals = code.co_nlocals + 1
    co_stacksize = code.co_stacksize + 4
    co_consts = [v for v in code.co_consts]
    id_set_addr_dict = {}
    code_block_addr_tab = []

    random.shuffle(code_block_id_tab)
    co_code = chr(dis.opmap['JUMP_FORWARD']) + \
        n2b(9 * code_block_id_tab.index(begin))

    for code_block_id in code_block_id_tab:
        co_consts += [code_block_id]
        id_set_addr_dict[code_block_id] = len(co_code)
        co_code += chr(dis.opmap['LOAD_CONST']) + n2b(len(co_consts) - 1) + chr(dis.opmap['STORE_FAST']) + n2b(
            len(co_varnames) - 1) + chr(dis.opmap['JUMP_ABSOLUTE']) + n2b(9 * len(code_block_id_tab) + 3)

    co_consts += [None]

    for i, code_block_id in enumerate(code_block_id_tab):
        code_block = code_blocks[code_block_id][0]
        next_code_block_id = 0
        if code_block_id in code_block_id_xref_dict:
            next_code_block_id = code_block_id_xref_dict[code_block_id]
        c = 0
        if len(code_block) >= 3:
            c = ord(code_block[-3])
        next_jmp = ''
        if next_code_block_id:
            next_jmp = chr(dis.opmap['JUMP_ABSOLUTE']) + \
                n2b(id_set_addr_dict[next_code_block_id])
        if c in dis.hasjabs:
            target_addr = b2n(code_block[-2:])
            for code_jmp_block_id in code_block_id_tab:
                if target_addr in code_blocks[code_jmp_block_id][1]:
                    code_blocks[code_block_id][0] = code_block[
                        :-2] + n2b(id_set_addr_dict[code_jmp_block_id]) + next_jmp
                    break

        elif c in dis.hasjrel:
            delta = b2n(code_block[-2:])
            target_addr = code_blocks[code_block_id][1][-1] + 1 + delta
            for code_jmp_block_id in code_block_id_tab:
                if target_addr in code_blocks[code_jmp_block_id][1]:
                    code_blocks[code_block_id][0] = code_block[:-2] + n2b(len(next_jmp)) + next_jmp + chr(
                        dis.opmap['JUMP_ABSOLUTE']) + n2b(id_set_addr_dict[code_jmp_block_id])
                    break

        else:
            code_blocks[code_block_id][0] = code_block + next_jmp

    random.shuffle(code_block_id_tab)
    code_block_tab = [code_blocks[v][0] for v in code_block_id_tab]
    code_block_size = len(''.join(code_block_tab))
    co_code += chr(dis.opmap['JUMP_FORWARD']) + n2b(code_block_size)

    code_block_addr_dict = {}
    for i, code_block in enumerate(code_block_tab):
        code_block_addr_dict[code_block_id_tab[i]] = len(co_code)
        co_code += code_block

    random.shuffle(code_block_id_tab)
    for i, code_block_id in enumerate(code_block_id_tab):
        co_code += chr(dis.opmap['LOAD_CONST']) + n2b(co_consts.index(code_block_id)) + chr(dis.opmap['LOAD_FAST']) + n2b(len(
            co_varnames) - 1) + chr(dis.opmap['COMPARE_OP']) + n2b(2) + chr(dis.opmap['POP_JUMP_IF_TRUE']) + n2b(code_block_addr_dict[code_block_id])
    co_code += chr(dis.opmap['LOAD_CONST']) + \
        n2b(len(co_consts) - 1) + chr(dis.opmap['RETURN_VALUE'])

    for i, v in enumerate(co_consts):
        if isinstance(v, types.CodeType):
            co_consts[i] = make_code_obfuscate(v)

    co_consts = tuple(co_consts)
    co_varnames = tuple(co_varnames)
    if len(co_code) > 0xffff:
        print '[ERROR]code is too long.'
    return types.CodeType(code.co_argcount, co_nlocals, co_stacksize, code.co_flags, co_code, co_consts, code.co_names, co_varnames, code.co_filename, code.co_name, code.co_firstlineno, code.co_lnotab)

f = open('ck.pyc', 'rb')
head = f.read(8)
r = f.read()
f.close()
code = marshal.loads(r)
final = make_junk_code(make_code_obfuscate(code))
f = open('out.pyc', 'wb')
f.write(head + marshal.dumps(final))
f.close()
