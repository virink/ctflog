import sys
from hashlib import sha256

current_account = ""
secret = '******************************'

def authenticate(cred_id, cred_pw):
    return sha256(secret+cred_id).hexdigest()

member_tbl = {'shenyue': authenticate('shenyue', "****************************")}

def menu():
    print "==== administration console ===="
    print "1. sign up"
    print "2. log in"
    print "3. private key generation"
    print "-1. command execution"

def get_cred():
    cred_id = raw_input("id: ")
    cred_pw = raw_input("pw: ")
    return (cred_id, cred_pw)

def sign_up():
    (cred_id, cred_pw) = get_cred()
    
    if member_tbl.has_key(cred_id):
        print "id already exists"
        return

    member_tbl[cred_id] = cred_pw
    print "successfully registered"

def login():
    global current_account
    
    (cred_id, cred_pw) = get_cred()
    if member_tbl.has_key(cred_id):
        if member_tbl[cred_id] == cred_pw:
            print "logged in as %s" % cred_id
            current_account = cred_id
            
        else:
            print "wrong password"
            
    else:
        print "id doesn't exist"

def member_key_generation():
    global current_account

    if current_account == "":
        print "need to log in to generate your private key"
        print "this private key doesn't take information from your password"
        print "because we are too worried about the plaintext password leaked... :'("
    else:
        cmd = raw_input("which command do you want to execute: ")
        key = authenticate(current_account+cmd, secret)
        print "generating your key associated with", current_account
        print "you can use the key to execute a command"
        __import__('time').sleep(1)
        print "your id+cmd combination results in", key
        print "Kindly reminder: please don't give your key to anyone"
    
def command_exec():
    cmd = raw_input("what command? ")
    cred_id = raw_input("who signed this command? ")
    key = raw_input("give me the signed document: ")

    print "ok, let me check if this sign is issued by this system"
    if authenticate(cred_id+cmd, secret) == key:
        if member_tbl.has_key(cred_id):
            print "ok, good good"
            print "flag is: ******************"
            return

    print "don't be fooled"
    return

if __name__ == "__main__":
    menu()

    choice_tbl = {
        '1': sign_up,
        '2': login,
        '3': member_key_generation,
        '-1': command_exec
        }
    
    try:
        while True:
            selection = raw_input("> ")
            choice_tbl[selection]()
        
    except Exception as e:
        print "?"
        sys.exit(0)

