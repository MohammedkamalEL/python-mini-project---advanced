import random,time


all_opration = ['+','-','*','/','**']


def round_play():
    while True:
        answer = input('how many round wou want? ')
        if answer.isdigit() and answer != '0':
            return int(answer)
        else:
            print('invaled input try agin ')


def play(range_limt):
    round_num = round_play()
    print('---------- satrt game ------------')
    while True:
        score = 0
        start_time = time.time()
        for i in range(round_num):
            print(f'round {i+1} of {round_num} \n')
            opration = random.choice(all_opration)
            num1 = random.choice(range_limt)
            num2 = random.choice(range_limt)
            
            ask_user = input(f'{num1} {opration} {num2} = ')
            expretion = f"{num1} {opration} {num2}"
            right_ans = eval(expretion)
            
            try:
                if float(ask_user) == right_ans:
                    score += 1
            except ValueError:
                print('invaled input try agin ')
                
        end_time = time.time()
            
        all_time_play = round(end_time - start_time,2)
        print(f'time is {all_time_play}s ')
            
        break
    print(f'done game you hane {score} of {round_num}')


def game_check(level):

    if level == 'easy':
        range_number = [i for i in range(1,11)]
        print('range number from 1 to 10')
        play(range_number)
    elif level == 'hard':
        range_number = [i for i in range(10,51)]
        print('range number from 10 to 50')
        play(range_number)
        
        
while True:
    mode_level_game = input('inter your level you want play in math: ( Easy - Hard ) ').lower()

    if mode_level_game.isdigit():
        print('try agin invaled input')
    elif mode_level_game in ['easy', 'hard']:
        game_check(mode_level_game)
        break
    else:
        print('try inter ( Easy - Hard)')
        


