import turtle


BOARD_HEIGHT = 6
BOARD_WIDTH = 7
START_X = -175
START_Y = 125
x=START_X
y=START_Y
CELL_SIZE = 50 # side length of the square
L=CELL_SIZE*8
W=CELL_SIZE*8
PLAYER1 = 'red'
PLAYER2 = 'blue'
BASE_COLOR = 'black'
board = [[0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7]]
cur_player = 1

def vert_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y-L)
    turtle.up()

def horiz_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+W,y)
    turtle.up()

def draw_board():
    one=range(0,8)
    two=range(0,8)
    x=START_X
    y=START_Y
    for me in one:
        vert_line(x,y)
        x=W/8+x
    x=START_X
    y=START_Y
    for group in two:
        horiz_line(x,y)
        y=L/8 - group*CELL_SIZE
        
draw_board()
