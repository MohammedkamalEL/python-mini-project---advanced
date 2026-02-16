import re 

with open('store.txt','r') as file:
    content = file.read()
    
def play_game():
    
    key_placeHolder = re.findall(r'\{(.*?)\}',content)
    user_inswer = {}
    print('-------- letes start game -------------')
    
    for _, item in enumerate(key_placeHolder):
        
        while True:
            answer = input(f'inter the {item}: ')
            if answer.isdigit():
                print('invaled input pleasee try agin')
            else:
                user_inswer[item] = answer
                break
            
    final_reslt = content.format(**user_inswer)
    print(final_reslt)         
        
play_game()


# lis = ['ali','noor','huda','mona']

# for i,item in enumerate(lis):
#     print(i, '--->', item, '\n \n')

# user_data = {"name":'mohammed Kamal', "age":"30" ,"wife":"Aisha"}

# text = 'hi {name} your age is : {age} youw white --> {wife}'.format(**user_data)

# print(text)

# 2:15
