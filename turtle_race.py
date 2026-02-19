import turtle, time, random

WIDTH, HEIGHT = 500, 500
COLOR = ['green','yellow','red','cyan','purple','black','pink'] 

def get_number_of_racers():
    while True:
        answer =  input('inter number in 1 - 7  ? ')
        if answer.isdigit():
            answer = int(answer)
        else:
            print('invaled input Try Agin! ')
            continue
        if 1 <= answer <= 7:
            return answer
        else:
            print('inter in range 1 to 7 ')

def creat_turtles(colerr):
    turtles = []
    spasing = WIDTH // (len(colerr)+ 1)
    for i, color in enumerate(colerr):
        race = turtle.Turtle()
        # race.speed(1)
        race.shape('turtle')
        race.left(90)
        race.penup()
        race.color(color)
        race.setpos(-WIDTH //2 + (i + 1) * spasing, -HEIGHT //2 + 20)
        race.pendown()
        turtles.append(race)
        # time.sleep(1)
    return turtles    

def race(color):
    turtle = creat_turtles(color)
    while True:
        for tur in turtle:
            move_random = random.randint(0,10)
            tur.forward(move_random) 
            _,y = tur.pos()
            if y > (HEIGHT / 2) - 20:
                return tur.pencolor()
                 
            
def screen_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT, startx=0,starty=0 )
    screen.title('welcome to mohammed game')
    # screen.bgcolor('red')

            
number_turtle =  get_number_of_racers()
screen_turtle()
 
random.shuffle(COLOR)
color = COLOR[:number_turtle]
win = race(color)
print(win)
time.sleep(3)   








race = turtle.Turtle()
# race.xcor()
# race.speed(1)
# # race.pos(-100.00,240.00)
# race.color('green')
# race.shape('turtle')
# race.penup()
# race.forward(200)
# race.right(90)
# race.forward(200)
# race.right(90)
# race.pendown()
# race.forward(200)
# race.right(90)
# race.forward(200)
# time.sleep(2)

