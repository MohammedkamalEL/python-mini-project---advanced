import random

MAX_LINE = 3

MAX_BIT = 100
MIN_BIT = 1

ROWS = 3
COL = 3

symbol = {"A":2,"B":4,"C":6,"D":8}
values_win = {"A":7,"B":5,"C":3,"D":1}

def get_slote_machine_spin(row , col, symbole_main):
    all_symbol = []
    
    for sy, count in symbole_main.items():
        for _ in range(count):
            all_symbol.append(sy)
    
    columns = []
    
    for _ in range(col):
        colum = []     
        crunt_symbole = all_symbol[:]
        for _ in range(row):
            value = random.choice(crunt_symbole)
            crunt_symbole.remove(value)
            colum.append(value)
        columns.append(colum)
    return columns
                   
def print_slote_machine(columns):
    for row in range(len(columns[0])):
        for i, item in enumerate(columns):
            if i != len(columns) -1:
                print(item[row], end =" | ")
            else:
                print(item[row], end="")         
        print('')

def deposit():
    while True:
        amount = input('inter money to play ? $')
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        else:
            print('\n invaled input try agin :) \n')

def get_lines():
    while True:
        line = input(f'inter the number Line you want to play from 1 to {MAX_LINE} ? ')
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                return line
            else:
                print(f'\n try agin should be in  ( 1 - ${MAX_LINE} ) on line :) \n')

        else:
            print(f'\n invaled input try agin ( 1 - ${MAX_LINE} ) :) \n')
        
def get_bit():
    while True:
        bit = input(f'inter the bit ( min: ${MIN_BIT} - max: ${MAX_BIT} ) ? ')
        if bit.isdigit():
            bit = int(bit)
            if MIN_BIT <= bit <= MAX_BIT:
                return bit
            else:
                print(f'\n try agin should be in ( min: ${MIN_BIT} - max: ${MAX_BIT} ) :) \n')

        else:
            print(f'\n invaled input try agin ( min: ${MIN_BIT} - max: ${MAX_BIT} ) :) \n')
    
def check_wins(columns, line, bit, values_win):
    winner = 0
    line_win = []
    for row in range(line):
        symbol = columns[0][row]
        for col in columns:
            if symbol != col[row]:
                break    
        else:
            winner += values_win[symbol] * bit
            line_win.append(row+1)
    return winner, line_win
    
def main():
    balance =  deposit()
    line = get_lines()
    
    while True:
        bit = get_bit()
        if balance < bit * line:
            print(f'you inter invaled range less the bit try agin, your crunt palance is :  ${balance}')
        else:
            break
    
    print(f'you Betting {bit} in {line} lines your total is {bit*line}')
    columns =  get_slote_machine_spin(ROWS,COL,symbol)
    print_slote_machine(columns)
    
    mony, line_win =  check_wins(columns, line, bit, values_win)
    balance += mony - (bit * line)
    
    print(f'you win ${mony} line wine ' , *line_win , f' your balance is: ==> {balance}')
    
    while True:
        ans = input('play agin :) ? ( Y - Q : quit game ) ').lower()
        if ans == 'q':
            quit()
        elif ans == 'y':
            main()
            break
        else:
            print('invaled input')
main()


# for i in [1,2,3,4,5,6,7,8]:
#     if i == 5:
#         continue
#     else:
#         print(i)
# else:
#     print('done')
# lis = [1,2,3,4,5,6,7,8]
# print(*lis)
