import turtle
from turtle import *

turtle.penup()
turtle.ht()
screen = turtle.getscreen()
screen.register_shape("marker.gif")
screen.register_shape("blue.gif")
class Marker(Turtle): 
	def __init__(self,x,y,colour,hit,visible):
		cv = turtle.getscreen()
		RawTurtle.__init__(self,cv)
		self.x=x
		self.y=y
		self.colour=colour
		self.hit=hit
		self.pu()
		if (visible == False):
			self.ht()
		if hit==True:  
			self.shape("marker.gif")
		else:
			self.shape("blue.gif")
		self.speed(0)
		self.goto(x,y)
#m = Marker(50,50,"red",True)
