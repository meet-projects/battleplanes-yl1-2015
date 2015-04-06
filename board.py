import Planes
from Planes import *
import Markers
from Markers import *

class Board():
	def __init__(self):
		self.planes = []
		self.markers = []
	def AddPlane(self,plane):
		self.planes.append(plane)
	def AddMarker(self,marker):
		self.markers.append(marker)
	def ShowAll(self):
		for plane in self.planes:
			plane.st()
		for marker in self.markers:
			marker.st()
	def HideAll(self):
		for plane in self.planes:
			plane.ht()
		for marker in self.markers:
			marker.ht()
	def MarkerExistsAtLoc(self,x,y):
		for marker in self.markers:
			if (marker.x == x and marker.y == y):
				return True
		return False
	def PlaneExistsAtLoc(self,x,y):
		for plane in self.planes:
			if (plane.sunk == True):
				continue
			if (x > plane.startX and x < plane.endX and y < plane.startY and y > plane.endY):
				return True
		return False
	def CheckIfPlaneSunk(self,x,y):
		for plane in self.planes:
			if (plane.sunk == True):
				continue
			if (x > plane.startX and x < plane.endX and y < plane.startY and y > plane.endY):
				count = 0
				for marker in self.markers:
					curX = marker.x
					curY = marker.y
					if (curX > plane.startX and curX < plane.endX and curY < plane.startY and curY > plane.endY):
						count += 1
				if (count == plane.size):
					plane.sunk = True
					return plane
				return None

