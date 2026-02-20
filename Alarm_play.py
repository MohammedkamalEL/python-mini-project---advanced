from playsound3 import playsound
import time,  keyboard
from threading import Thread


is_runing = True

def check_sound():
    global is_runing
    
    keyboard.wait('s')
    is_runing = False
    print('\nyou stop play sound')


def alarm(second = 10):
    global is_runing

    stop_thred= Thread(target=check_sound,daemon=True)
    stop_thred.start()
    
    while second > 0 and is_runing:
        minu,sec = divmod(second,60)
        print(f'\ralarm play in {minu:2d}:{sec:02d}', end='')
        time.sleep(1)
        second -= 1
        
    sound = playsound('play.wav')
    sound.stop()
        

minutes = int(input('inter how many minutes the alrm play after it? '))

second = minutes * 60
alarm()

# print(125 // 60)# 2
# print(125 % 60) # 5
# print(125 / 60) # 2.084444
# print(divmod(130,60)) # 60 * 2 = 120 min = 10  (2,10) / 
# print(divmod(500,60))