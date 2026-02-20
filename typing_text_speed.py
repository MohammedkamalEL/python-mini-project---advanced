import  time,random,curses


list_line=['welcome to mohammed kamal game work is full stack developer','mohammed kamal is love to be agood person in his life']


def start(stdscr):
    stdscr.clear()
    stdscr.addstr(0,20,'--------------------- welcome to mohammed kamla speed type game :) -------------------- \n')
    stdscr.refresh()
    stdscr.getkey()
    

def display_text(stdscr,crunt_text,target_text,wpn=0):
    stdscr.addstr(target_text)
    stdscr.addstr(2,0, f'WPM ---> {wpn}')
    for i, char in enumerate(crunt_text):
        if target_text[i] == char:
            stdscr.addstr(0,i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0,i, char, curses.color_pair(2))

        
def wpn_test(stdscr):
    target_text = random.choice(list_line)
    crunt_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True:
        elapes_time = max(time.time() - start_time,1) / 60 
        
         
        stdscr.addstr(f'{target_text}')
        
        for char in crunt_text:
            
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.clear()
        wpm = round((len(crunt_text)) / elapes_time) / 5
        display_text(stdscr,crunt_text,target_text,wpm)        
        stdscr.refresh()
        
        if len(crunt_text) == len(target_text):
            stdscr.nodelay(False)
            break
            
        try:
            key = stdscr.getkey()
        except :
            continue
        
        if ord(key) == 27:
            break
        if key in ('KEY_BACKSPACE', '\b','\x7f'):
            try:
                crunt_text.pop()
            except IndexError:
                stdscr.addstr('error')
        elif len(crunt_text) < len(target_text):
            crunt_text.append(key)
            
    
        
    
    
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start(stdscr)
    wpn_test(stdscr)
    
    stdscr.addstr(3,0,'\n you done press any key and out ')
    stdscr.getkey()

    
curses.wrapper(main)
