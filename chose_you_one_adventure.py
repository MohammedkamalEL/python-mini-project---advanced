
import random

print('--- Welcome to Mohammed\'s Adventure Game ---')

has_map = False

def road_game(user_input):
    global has_map
    # random_number  = random.randint(0,3)
    if user_input == 'a':
        answer = input('You find a hungry lion! \n (A) - Fight the lion \n (B) - Climb a tree \n -> ').lower()
        if answer == 'a':
            print('The lion was too strong!')
            return 'Game Over'
        elif answer == 'b':
            has_map = True
            print('Safe! You found a map hidden in the branches. Now you returned to the path.') 
            return 'Continue'
        
    elif user_input  == 'b':
        answer = input('You find a dark Cave. \n (A) - Go inside \n (B) - Keep walking \n -> ').lower()
        if answer == 'b':
            print('You got lost in the forest.')
            return 'Game Over'
        elif answer == 'a':
            if has_map:
                print('Using the map, you found the hidden treasure!')
                return 'W I N !'
            else:
                print('It\'s too dark and you don\'t have a map/light to guide you. You stumbled and fell!')  
                return 'Game Over'
            
    return 'Invalid'
            

while True:
    first_way = input('\nDo you want to play? Yes (Y) No (N): ').lower()
    want_play = False
    
    if first_way.isdigit():
        print('dont inter number try agin')
        continue
    elif first_way == 'y':
        want_play = True
        print('--- Game Started ---')
    elif first_way == 'n':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print('Please enter Y or N')
        continue
    
    if want_play:
        answer = input('\nYou are at a crossroads. Where do you go? \n (A) - The Jungle (Gaba) \n (B) - The Coast (Alsahel) \n -> ').lower()
        
        if answer in ['a','b']:
            result =  road_game(answer)
            if result == 'W I N !':
                print('*** CONGRATULATIONS! YOU WON! ***')
                break
            elif result == 'Game Over':
                print('*** GAME OVER ***')
                break
            elif result == 'Continue':
                continue
            else:
                print('Invalid input, please choose A or B. \n')
            
    
    # 56:4


