import random, sys

# print(random.randrange(0,11,2))
# print(random.randint(0,10))

top_range_number = input('Type Number of Range :) ? ')

# print(str(top_range_number).isdigit())


random_number = 0

# list_of_number = []

user_try_guess = 0

if   str(top_range_number).isalpha() or int(top_range_number) <= 0 :
    print('you inter invaled input ')
    sys.exit()
else:
    top_range_number = int(top_range_number)
    random_number = random.randint(0 ,top_range_number)
    
# for i in range(top_range_number+1):
#     new_arry =   list_of_number
#     new_arry.append(i)
    
    

while True:
    answer = input('now you inter number in range 0 and ' + str(top_range_number) + ' and shouls gese right number of this number --> ').strip()
    user_try_guess += 1
    
    if answer.isdigit():
        answer = int(answer)
        if answer == random_number:
            print('you win after', user_try_guess, 'try')
            break
        elif answer > random_number:
            print('you inter above random number')
        else:
            print('you inter less random number')
    
    elif answer.isalpha() :
        print(answer , 'not right you inter string ')
        # continue
    else:
        print('شغل مختلف ')

print('program done')   

    
#  39:49