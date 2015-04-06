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
		
		curX = 0
		curY = 0
		if (self.size % 2 == 0 and self.tilt == "v"):
			curX = -400 + col * 50 + 25
			curY = 200 + row * 50 - 50
		elif (self.size % 2 == 0 and self.tilt == "h"):
			curX = -400 + col * 50
			curY = 200 + row * 50 - 25
		else:
			curX = -400 + col * 50 + 25
			curY = 200 + row * 50 - 25
		self.goto(curX, curY)
		self.x = curX
		self.y = curY
		self.ondrag(self.passfunc)
		self.onrelease(self.passfunc)
		self.onclick(self.clicked)
		
		if (self.tilt == "v"):
			self.startX = curX - 25
			self.endX = curX + 25
			self.startY = curY + self.size * 25
			self.endY = curY - self.size * 25
		else:
			self.startX = curX - self.size * 25
			self.endX = curX + self.size * 25
			self.startY = curY + 25
			self.endY = curY - 25
		if (self.startX >= -400 and self.endX <= 0 and self.startY <= 200 and self.endY >= -200):
			self.loc = str(col) + "," + str(row)
		else:
			self.loc = ""
		#print(str(self.startX) + "," + str(self.endX) + "     " + str(self.startY) + "," + str(self.endY))
	def clicked(self,x,y):
		self.ondrag(self.goto)
		self.onrelease(self.released)
		self.onclick(self.passfunc)
	def passfunc(self,x,y):
		pass

#m = Plane(250,150,"1",False,"v")
#b = Plane(150,150,"2",False,"h")
#l = Plane(350,150,"3",False,"v")
#p = Plane(50,150,"1",False,"h")


#turtle.mainloop()



