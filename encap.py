# Using OOP in Python, we can restrict access to methods and variables. 
# This prevents data from direct modification which is called encapsulation.
#  In Python, we denote private 
# attributes using underscore as the prefix i.e single _ or double __.





# private method
class car:
	def __init__(self):
		self.__bluecar()
	def drive(self):
		print("wheel")
	def __bluecar(self):
		print("horn")
obj=car()
obj.drive()
#obj.__bluecar()


# private variable
class car:
	__maxspeed=0
	__name=""
	def __init__(self):
		self.__maxspeed=200
		self.__name="supercar"
	def drive(self):
		print("speed checking",self.__maxspeed)
	def drive1(self,speed):
		self.__maxspeed=speed
		print("speed checking",self.__maxspeed)
obj=car()
obj.drive()
obj.drive1(100)
