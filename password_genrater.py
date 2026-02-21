import random,string

def genrat_password(length, hav_number=True, has_special=True):
    leater = string.ascii_letters
    num = string.digits
    spesial = string.punctuation

    charecter = leater
    if hav_number:
        charecter += num
    if has_special:
        charecter += spesial
        
    password = ''.join(random.choice(charecter) for _ in range(length)) 
    # pa = "".join(list(random.choice(charecter) for i in range(length)))

    # for _ in range(length):
    #     password += random.choice(charecter)
    return password

def add_to_file(password):
    with open('password_genaret.txt','a') as file:
        file.write(password + '\n')


answer =  int(input('inter length of password you want? '))
numbers =  input('inter numbers of password you want? (y/n) ') == 'y'
special =  input('inter special of password you want? (y/n) ') == 'y'

# if numbers != 'y' or special != 'y':
#     numbers = False
#     special= False
# else:
#     numbers = True
#     special = True

# num = True if numbers.lower() == 'y' else False
# spe = True if special.lower() == 'y' else False

# num = (numbers.lower() == 'y')
# spe = (special.lower() == 'y')

print(numbers,special)
rasswprd =  genrat_password(answer,numbers,special)
add_to_file(rasswprd)
print(rasswprd)
