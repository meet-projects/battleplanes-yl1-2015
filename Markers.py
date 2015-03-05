import turtle
turtle.register_shape("image.gif")
class Markers(Turtle): 
	def __init__(self,loc,colour,hit):
		RawTurtle.__init__(self)
		self.loc=loc
		self.colour=colour
		self.hit=hit
		self.shape("image.gif")
Markers m = new Markers("A1", "red",true)
	





