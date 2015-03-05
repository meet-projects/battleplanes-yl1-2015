import turtle
turtle.up()


def LineUp(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.goto(x,y+702)
    turtle.up()

def lineLeft(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle(x-1002,y)
    turtle.up()

one=range(0,8)
two=range(0,7)

#defining/printing of vertical lines
y=143
x=-501

for ameen in one:
    LineUp(x,-351)
    x=x+y

#defining/printing of horizontal lines
y=-351
x=117

for adi in two:
    lineLeft(501,y)
    y=y+x
    













turtle.mainloop()
