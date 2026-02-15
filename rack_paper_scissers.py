import random, sys

print('start game')

options = ('rock', 'paper', 'scissors')

equel = 0
user_win =0
computer_win =0

while True:
    computr_choise = random.choice(options)
    user_input = input('inter your choise [ rock - paper - scissors ] or Q to quick the game --> ').lower()

    if user_input not in options:
        if user_input == 'q':
            break
        else:
            print('invaled input try agin! ')
            continue
    
    if user_input == computr_choise:
        equel += 1
        print(' equvlent :) ')
        continue
    elif (user_input == 'rock' and computr_choise == 'scissors') or (user_input == 'scissors' and computr_choise == 'paper') or (user_input == 'paper' and computr_choise == 'rock') :
        user_win += 1
        print(f'=====\n you win \n equel ==> {equel} , user_win ==> {user_win} , computer wine ==> {computer_win}  \n=====')
    else:
        computer_win += 1
        print(f"you lose sorry try agin computr pik {computr_choise} and you {user_input}")
    


print(f'done game equel ==> {equel} , user_win ==> {user_win} , computer wine ==> {computer_win} ')