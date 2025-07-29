from cryptography.fernet import Fernet


# # To make key. Only used once and thats it.
# def write_key():
#     key = Fernet.generate_key()
#     with open ("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Maser password feature not working. Check documentation of fernet
#master_pwd = input ("What is the master password? ")
key = load_key() #+ master_pwd.encode() # Encode converts to bytes
fer = Fernet(key)




def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username:",user, "| Password:", fer.decrypt(passw.encode()).decode())
        
        
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # Added decode cuz I tried to convert the whole thing to string but since its in bytes, it stored the password with format b'password'.

while True:
    mode = input("Would you like to add a new password or view existing ones? (add, view). Press q to quit. ").strip().lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter a valid mode.")
        continue
    
    

