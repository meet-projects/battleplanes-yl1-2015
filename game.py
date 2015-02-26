#This is a demo project for meet Yearlong 2014-15 Y1
from turtle import *
import tkinter.messagebox
import tkinter
import random
import math

#These Four variables are the borders of the game world
screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

#Here we DEFINE the class Astroid (later we will use this Class to create astroids)
class Asteroid(Turtle):
    # __init__ is going to be called per every new astroid we create a new astroid
    def __init__(self,canvas,dx,dy,x,y,size):
        RawTurtle.__init__(self,canvas) #this line keep it as it is
        # we define the properties of the astroid
        self.penup()
        self.goto(x,y)
        self.size = size
        self.dx = dx
        self.dy = dy
        self.shape("rock"+str(size))

    def getSize(self):
        return self.size
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy
    
    def setDX(self,dx):
        self.dx = dx
        
    def setDY(self,dy):
        self.dy = dy
        
    def move(self):
        x = self.xcor() # this line gives me the current x cordination of the astroid and saves it in variable x
        y = self.ycor() # this line gives me the current y cordination of the astroid and saves it in variable y
        # this werid calculation that will see if the atroid reached the end of the screen of both sides right and left to make it show up in the other side
        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX 
        # this werid calculation that will see if the atroid reached the end of the screen of both sides top and buttom to make it show up in the other side
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        # then we tell the astroid to go to the new location
        self.goto(x,y)
   
    def getRadius(self):
        return self.size * 10 - 5

class SpaceShip(Turtle):
    def __init__(self,canvas,dx,dy,x,y):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.color("purple")
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.shape("ship")

    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        
        self.goto(x,y)

    def fireEngine(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        self.dx = self.dx + x
        self.dy = self.dy + y
   
    def getRadius(self):
        return 2
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy

    def turnLeft(self):
        self.setheading(self.heading()+7)

    def turnRight(self):
        self.setheading(self.heading()-7)

#this function is not inside any class and this function calculates a circle around the turtles to check if they hit each other
def intersect(object1,object2):
        dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
        
        radius1 = object1.getRadius()
        radius2 = object2.getRadius()
        
        # The following if statement could be written as 
        # return dist <= radius1+radius2
        if dist <= radius1+radius2:
            return True
        else:
            return False

def main():
    # These 4 lines just to prepare the window of the game, no need to change them
    root = tkinter.Tk()
    root.title("Asteroids!")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)

    #Here we prepre the new shapes of the game
    t = RawTurtle(cv)
    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("rock3",((-20, -16),(-21, 0), (-20,18),(0,27),(17,15),(25,0),(16,-15),(0,-21)))
    screen.register_shape("rock2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
    screen.register_shape("rock1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
    screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
    screen.register_shape("bullet",((-2,-4),(-2,4),(2,4),(2,-4)))
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    t.ht()
    
    # this function when it is called the game will exit
    def quitHandler():
        root.destroy()
        root.quit()

    #here we are creating the button that you will see it on the right side of the game called Quit
    # the part it says command=quitHandler is telling the button when we click it to run the function quitHandler that we defined above
    quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
    quitButton.pack()
    
    screen.tracer(10)
    
    # here we are using the class we defined above to create the spaceShip
    ship = SpaceShip(cv,0,0,0,0)
    
    # This is preparing a list that we will store all the astroids in it
    asteroids = []
    
    # this loop runs 5 times and each time it creates an astroid and adds it to the list of astroids
    for k in range(5):
        # preparing random variables 
        dx = random.random() * 6 - 3 #random speed in x (change in x)
        dy = random.random() * 6 - 3 #random speed in y (change in y)
        x = random.random() * (screenMaxX - screenMinX) + screenMinX # random starting x location
        y = random.random() * (screenMaxY - screenMinY) + screenMinY # random starting y location
        size = random.random() * 3 +1 # random size (1 or 2 or 3) since we only defined 3 shapes of astroids

        # here we create the astroid with the random variables we defined above
        asteroid = Asteroid(cv,dx,dy,x,y,int(size))

        # here we are adding the astroid to the astroids list
        asteroids.append(asteroid)

    # here we a function that we will call it every 5 millisecond (THIS IS WHAT CODE KEEPS RUNNING WHILE THE GAME IS OPEN)
    # this we call it GAME LOOP
    # GAME LOOP (BEGIN)
    def play():
        # Tell all the elements of the game to move
        # Tell the ship to move
        ship.move()
        # go (loop) though each astroid in the astroids list and tell it to move as well check if it is toucing the ship
        for asteroid in asteroids:
            if (intersect(ship,asteroid)):
                print("You Failed")
                quitHandler()
            asteroid.move()
        # Set the timer to go off again in 5 milliseconds
        screen.ontimer(play, 5)
    # GAME LOOP (ENDS)

    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play,5)
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the left arrow key is pushed in the keyboard
    screen.onkeypress(ship.turnLeft,"Left")
    # this means call the defined function in class spaceShip turrnRight for the ship everytime the right arrow key is pushed in the keyboard
    screen.onkeypress(ship.turnRight,"Right")
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the up arrow key is pushed in the keyboard
    screen.onkeypress(ship.fireEngine,"Up")
    
    screen.listen()
    tkinter.mainloop()
  
if __name__ == "__main__":
    main()
  