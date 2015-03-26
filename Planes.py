import turtle

class Planes(Turtle):
	def __init__(self,loc,colour,hit,shape):
		RawTurtle.__init__(self)
		self.loc=loc
		self.colour=colour
		self.hit=hit
		self.shape=shape
	
