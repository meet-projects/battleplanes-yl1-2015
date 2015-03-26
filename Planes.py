import turtle
from turtle import *

turtle.ht()

screen = turtle.getscreen()
screen.register_shape("plane1v.gif")
screen.register_shape("plane2v.gif")
screen.register_shape("plane3v.gif")
screen.register_shape("plane1h.gif")
screen.register_shape("plane2h.gif")
screen.register_shape("plane3h.gif")

class Plane(Turtle):
	def __init__(self,x,y,size,sunk,tilt):
		cv = turtle.getscreen()
		RawTurtle.__init__(self,cv)
		self.x=x
		self.y=y
		self.sunk=sunk
		self.shape("plane"+size+tilt+".gif")
		self.pu()
		self.goto(x,y)



#m = Plane(250,250,"1",False,"v")
#b = Plane(150,150,"2",False,"h")
#l = Plane(350,350,"3",False,"v")
#p = Plane(50,50,"1",False,"h")

#turtle.mainloop()



