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
		self.tilt = tilt
		self.size = int(size)
		self.speed(0)
		self.shape("plane"+size+tilt+".gif")
		self.pu()
		self.goto(x,y)
		self.loc = "";
	def released(self,x,y):

		self.x = x
		self.y = y
		col = int((x + 400) / 50)
		row = int((y - 200) / 50)
		print(col,row)
		if (self.size % 2 == 0 and self.tilt == "v"):
			self.goto(-400 + col * 50 + 25, 200 + row * 50 - 50)
		elif (self.size % 2 == 0 and self.tilt == "h"):
			self.goto(-400 + col * 50, 200 + row * 50 - 25)
		else:
			self.goto(-400 + col * 50 + 25, 200 + row * 50 - 25)

		self.loc = str(col) + "," + str(row)
	def passfunc(self,x,y):
		pass

#m = Plane(250,150,"1",False,"v")
#b = Plane(150,150,"2",False,"h")
#l = Plane(350,150,"3",False,"v")
#p = Plane(50,150,"1",False,"h")


#turtle.mainloop()



