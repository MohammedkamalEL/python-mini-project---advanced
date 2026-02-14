import random, sys

# print(random.randrange(0,11,2))
# print(random.randint(0,10))

top_range_number = input('Type Number of Range :) ? ')

# print(str(top_range_number).isdigit())


random_number = 0

list_of_number = []

user_try_guess = 0

if   str(top_range_number).isalpha() or int(top_range_number) <= 0 :
    print('no')
    sys.exit()
else:
    top_range_number = int(top_range_number)
    random_number = random.randint(0 ,top_range_number)
    
for i in range(top_range_number+1):
    new_arry =   list_of_number
    new_arry.append(i)
    
while True:
    answer = input('now you inter number in range ' + str(list_of_number) + ' and shouls gese right number of this number --> ')
    user_try_guess += 1
    
    if str(answer).isalpha() :
        print('you inter str rather than number OR ')
        break
    elif int(answer) < 0:
        print('you inter less than 0')
        continue
        
    if int(answer) == random_number:
        print('you guesses right Number after ', user_try_guess , 'guess')
        # print(answer , random_number,  user_try_guess)
        break
    elif int(answer) >  random_number:
        print('you inter above random number')
        continue
    else:
        print('you inter less random number')
        continue
    
print('done')
    
    
    
 