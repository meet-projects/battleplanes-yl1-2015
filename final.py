import turtle
from turtle import *
import board
from board import *
import Markers
from Markers import *
import Planes
from Planes import *

turtle.speed(0)
turtle.ht()

def buildboard(startX,startY):
	for y in range(0,9):
		drawhorizline(startX, (startY - y*50))
	for x in range(0,17):
		drawverticline((startX + x*50), startY,400)
	for x2 in range(398,403):
		drawverticline((startX + x2), startY+50,500)
	lets = ["A", "B", "C", "D", "E", "F", "G", "H"]
	for x in range(0,8):
		turtle.goto(startX - 25, startY - 50 - x*50)
		turtle.write(lets[x], False,"center",font=("Ariel",25,"normal"))
	for x in range(0,8):
		turtle.goto(startX + 825, startY - 50 - x*50)
		turtle.write(lets[x], False,"center",font=("Ariel",25,"normal"))
	for x in range(1,9):
		turtle.goto(startX + 25 + (x-1)*50, startY )
		turtle.write(x, False,"center",font=("Ariel",25,"normal"))
		turtle.goto(startX + 800 - 25 - (x-1)*50, startY)
		turtle.write(x, False,"center",font=("Ariel",25,"normal"))
	for x in range(1,9):
		turtle.goto(startX + 25 + (x-1)*50, startY - 450)
		turtle.write(x, False,"center",font=("Ariel",25,"normal"))
		turtle.goto(startX + 800 - 25 - (x-1)*50, startY - 450)
		turtle.write(x, False,"center",font=("Ariel",25,"normal"))
def drawhorizline(x,y):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x + 800,y)
	turtle.pu()
def drawverticline(x,y,height):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x, y-height)
	turtle.pu()

buildboard(-400,200)

for x in range(0,5):
	m1 = Plane(-300,-300,str(x % 3 + 1),False,"v")
	m1.ondrag(m1.goto)
	m1.onrelease(m1.released)

turtle.mainloop()
