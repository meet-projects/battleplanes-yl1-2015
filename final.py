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
boardpl1 = Board()
boardpl2 = Board()

PLAYER_TURN = 1
START = True
SWITCH_TEXT = "START"
fHitMarkerThisTurn = False

turtle.pu()
turtle.goto(-75,300)
turtle.pd()
turtle.goto(75,300)
turtle.goto(75,250)
turtle.goto(-75,250)
turtle.goto(-75,300)
turtle.pu()
turtle.goto(0,250)
turtle.write("START", False,"center",font=("Ariel",25,"normal"))
turtle.goto(0,350)
turtle.write("PLAYER " + str(PLAYER_TURN), False, "center", font=("Ariel",25,"normal"))

allplanes = [];
def DrawFirstPlanes():
	global allplanes
	allplanes = []
	for x in range(0,3):
		m1 = Plane(-300 + x * 100, -300,str(x % 3 + 1),False,"v")
		m1.onclick(m1.clicked)
		m2 = Plane(0 + x*150,-300,str(x % 3 + 1),False,"h")
		m2.onclick(m2.clicked)
		allplanes = allplanes + [m1, m2]

def startbutton():
	global SWITCH_TEXT
	global PLAYER_TURN
	global allplanes
	global START
	global boardpl2
	global boardpl1
	global fHitMarkerThisTurn
	if (SWITCH_TEXT == "START" and START == True):
		DrawFirstPlanes()
		SWITCH_TEXT = "END"
	elif (SWITCH_TEXT == "END" and START == True):
		ourboard = Board()
		for x in allplanes:
			x.onclick(x.passfunc)
			if (x.loc != ""):
				ourboard.AddPlane(x)
			else:
				x.ht()
		ourboard.HideAll()
		if PLAYER_TURN == 2:
			boardpl2 = ourboard
			START = False
			PLAYER_TURN = 1
		else:
			boardpl1 = ourboard
			PLAYER_TURN = 2
		SWITCH_TEXT = "START"
	elif (SWITCH_TEXT == "START" and START == False):
		ourboard = []
		if (PLAYER_TURN == 2):
			ourboard = boardpl2
		else:
			ourboard = boardpl1
		ourboard.ShowAll()
		SWITCH_TEXT = "END"
	elif (SWITCH_TEXT == "END" and START == False):
		ourboard = []
		if (PLAYER_TURN == 2):
			ourboard = boardpl2
			PLAYER_TURN = 1
		else:
			ourboard = boardpl1
			PLAYER_TURN = 2
		ourboard.HideAll()
		SWITCH_TEXT = "START"
		fHitMarkerThisTurn = False
	turtle.pensize(45)
	turtle.pu()
	turtle.goto(50,275)
	turtle.pd()
	turtle.pencolor("white")
	turtle.goto(-50,275)
	turtle.pu()
	turtle.goto(-75,375)
	turtle.pd()
	turtle.goto(75,375)
	turtle.pensize(1)
	turtle.pencolor("black")
	turtle.pu()
	turtle.goto(0,250)
	turtle.write(SWITCH_TEXT, False,"center",font=("Ariel",25,"normal"))
	turtle.goto(0, 350)
	turtle.write("PLAYER " + str(PLAYER_TURN), False, "center", font=("Ariel",25,"normal"))

def ScreenClicked(x,y):
	global START
	global PLAYER_TURN
	global boardpl1
	global boardpl2
	global fHitMarkerThisTurn
	global SWITCH_TEXT
	if (x > -75 and x < 75 and y > 250 and y <300):
		startbutton()
	if (x < 0 or x > 400 or y > 200 or y < -200):
		pass
	elif (START == True):
		pass
	elif (fHitMarkerThisTurn == False and SWITCH_TEXT == "END"):
		col = int(x / 50)
		row = int((y + 200) / 50)
		# check if the other person's board..
		curboard = []
		otherboard = []
		if (PLAYER_TURN == 1):
			curboard = boardpl1
			otherboard = boardpl2
		else:
			curboard = boardpl2
			otherboard = boardpl1
		
		if (curboard.MarkerExistsAtLoc(25 + col*50, - 175 + row*50)):
			return
		
		color = "blue"
		hit = False;
		
		if (otherboard.PlaneExistsAtLoc(-25 - col*50, - 175 + row*50)):
			color = "red"
			hit = True
		
		m = Marker(25 + col*50, - 175 + row*50,color,hit,True)
		m2 = Marker(-25 - col*50, - 175 + row*50,color,hit,False)
		
		curboard.AddMarker(m)
		otherboard.AddMarker(m2)
		
		sunkPlane = otherboard.CheckIfPlaneSunk(-25 - col*50, - 175 + row*50)
		if (sunkPlane != None):
			newPlane = Plane(-sunkPlane.x, sunkPlane.y, str(sunkPlane.size), sunkPlane.sunk, sunkPlane.tilt)
			curboard.AddPlane(newPlane)
			
		fHitMarkerThisTurn = True

turtle.onscreenclick(ScreenClicked)


turtle.mainloop()
