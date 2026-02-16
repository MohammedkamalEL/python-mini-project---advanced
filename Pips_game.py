import random



while True:
    anser = input('inter number beween ( 2 - 4 ) players ')
    if anser.isdigit():
        anser = int(anser)
        if 2 <= anser <= 4:
            print('done players is --> ', anser)
            break
        else:
            print('should be between 2 - 4 try agin ')
    else:
        print('invaled input dode ! ')


scores = [0 for _ in range(anser)]
current_player = 0
game_over = False
    
def rand():
    return random.randint(1,6)
    
print('---- player one start game -----')

while game_over == False:
    
    input(f'\nplayer {current_player + 1} press enter ')
    random_num = rand()
    print('random_num --> ', random_num)
    
    if random_num == 1:
        scores[current_player] = 0
        print(f'random is --> {random_num} sorry you lose  all schore ')
        continue
    else:
        scores[current_player] += random_num
        print(f'player {current_player + 1} your scor Now is --> {scores[current_player]} ')
        
        if scores[current_player] >= 20:
            print(f'you win  player {current_player + 1} !')
            game_over = True
    
    print('your scroe now is :', scores[current_player])  
      
    current_player = (current_player + 1) % len(scores)
          
print('done game ')


 
 
 
 
    # if play_now == 1:
    #     input('player one press enter ')
    #     random_num = rand()
    #     print('random_num --> ', random_num)
    #     if random_num == 1:
    #         player_1_score = 0
    #         print(f'random is --> {random_num} sorry you lose  all schore ')
    #         play_now = 2
    #         continue
    #     else:
    #         player_1_score = random_num + player_1_score
    #         print(f'player 1 your scor Now is --> {player_1_score} more then 20 ')
    #         if player_1_score >= 20:
    #             print('you win  player 1 !')
    #             break
    #         else:
    #             play_now = 2
    #             continue
                    
                      
    #     # break
    # elif play_now == 2:
    #     input('player two press enter ')
    #     random_num = rand()
    #     print('random_num', random_num)
    #     if random_num == 1:
    #         player_2_score = 0
    #         print(f'random is --> {random_num} sorry you lose  all schore ')
    #         play_now = 1
    #         continue
    #     else:
    #         player_2_score = random_num + player_2_score
    #         print(f'player 2 your scor Now is --> {player_2_score} more then 20 ')
    #         if player_2_score >= 20:
    #             print('you win  player 2 !')
    #             break
    #         else:
    #             play_now = 1
    #             continue
    
    # 1:59
     