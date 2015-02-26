#import turtle 

#class board:
	#def __init__(self,x,y,vertline,horline):

import turtle 
x=-100
y=-100
def table(x,y):

	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x+200,y)
	turtle.goto(x+200,y-200)
	turtle.goto(x,y-200)
	turtle.goto(x,y)
	
table(x,y)
turtle.mainloop()

