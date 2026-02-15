import sys
from cryptography.fernet import Fernet

# pwd = input('inter the master password : ')

'''
def rite_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as file:
        file.write(key)
'''
        
def load_key():
    return open('key.key','rb').read()


key = load_key() 
# print(key)
f = Fernet(key)
    
def view():
    try:   
        with open('password.txt','r') as file:
            for line in file:
                data = line.strip()
                
                user , password_encrypted = data.split('|') 
                password_encrypted = password_encrypted.strip()
                
                decrypted_password = f.decrypt(password_encrypted.encode()).decode()
                
                print(f'user --> {user} | password --> {decrypted_password}\n')
    except FileNotFoundError:
        print("لا يوجد ملف كلمات مرور بعد. قم بإضافة واحدة أولاً.")

def add():
    name = input('inter your name ')
    password = input('inter your password ')
    encrypted_pwd = f.encrypt(password.encode())
    
    with open('password.txt',"a") as file:
        file.write( name + ' | ' + encrypted_pwd.decode() + '\n')    
    

while True:
    mode = input('would you like to view password --> (V) or add password --> (A)  or (Q) to exit ').lower()

    if mode == 'v':
        view()
    elif mode == "a":
        add()
    elif mode == 'q':
        sys.exit()
    else:
        print('invaled input tyr agin ')
        continue


# 1:37