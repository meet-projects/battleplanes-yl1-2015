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


