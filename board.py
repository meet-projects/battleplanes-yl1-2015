import turtle 
class Board():
	def _init_(self,x,y,widght,height,markers,colour):
		RawTurtle._init_(self)
		self.penup()
		self.goto(x,y)
		self.widght=widght
`		self.height=height
		self.colour=colour

		
		
