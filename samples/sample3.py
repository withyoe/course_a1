import turtle
import random

turtle.bgcolor('white')

t = turtle.Turtle()

# draw finish line
START_POS = 0
DISTANCE = 350
FINISH_LINE_SIZE = 10
P1_COLOR = 'green'
P2_COLOR = 'red'

def draw_square(color, pos, size):
    t.pencolor(color)
    t.penup()
    t.goto(pos)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(size)
    t.end_fill()

def draw_finish_line(y):
    for i in range (6):
        if i % 2 == 0:
            draw_square('black', (DISTANCE, y - FINISH_LINE_SIZE * i), FINISH_LINE_SIZE)
        else:
            draw_square('black', (DISTANCE + FINISH_LINE_SIZE, y - FINISH_LINE_SIZE * i), FINISH_LINE_SIZE)

    t.penup()


#player 1
draw_finish_line(100)

#player 2
draw_finish_line(-100)

p1 = t.clone()
p1.color(P1_COLOR)
p1.shape('turtle')
p1.penup()
p1.pencolor(P1_COLOR)
p1.goto(START_POS, 70)

p2 = t.clone()
p2.color(P2_COLOR)
p2.shape('turtle')
p2.penup()
p2.pencolor(P2_COLOR)
p2.goto(START_POS, -130)

#main loop
winner = False
take_turn = False

random.seed(6)
while winner == False:
    if take_turn == False:
        p1.pendown()
        input("Pemain 1 tekan sembarang tombol untuk melempar dadu")
        dice = random.randint(1, 6)
        print(dice)
        p1.forward(dice * 10)
        take_turn = True

    p1_xpos = p1.pos()
    p2_xpos = p2.pos()

    if (p1_xpos[0] >= DISTANCE):
        winner = True 
        print("Pemain 1 pemenangnya")
    
    if take_turn == True and winner == False:
        p2.pendown()
        input("Pemain 2 tekan sembarang tombol untuk melempar dadu")
        dice = random.randint(1, 6)
        print(dice)
        p2.forward(dice * 10)
        take_turn = False
    
    if (p2_xpos[0] >= DISTANCE):
        winner = True
        print("Pemain 2 pemenangnya")


input("Press any key to end the game!")