import sys

print(' welcome to Moh_Kamal quiz game ')

plauing = input('wont to play my game YES ==>(Y) NO ==>(N) ? :) ')

if plauing == "N":
    print('thanks and done ')
    sys.exit()
elif plauing.lower() == "y" or 'yes':
    print('start')
else:
    print('your input is wrong')
    sys.exit()
    
right_answer = 0

def Q_AND_A(answer_input, quite):
    global right_answer
    Q_AND_A.colls += 1
    answer = input(answer_input)
    if quite == answer.lower():
        right_answer +=1
        
Q_AND_A.colls = 0

Q_AND_A('what is your name ? ','moh')

Q_AND_A('what cpu stand form ? ','center process unit')

print(f'your inser is {right_answer} of {Q_AND_A.colls}')