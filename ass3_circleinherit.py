#Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area.

class Radius:
	def __init__(self,rad):
		self.rad=rad
		print("in radius\n" "radius=",self.rad)	

class Circle(Radius):
	def __init__(self,ob):
		print("@circle")
	
	
	def comp_area(self,ob):
		self.area=(22*ob.rad*ob.rad)/7
		print("area =",self.area)


obj=Radius(int(input("enter radius: ")))
ob=Circle(obj)
ob.comp_area(obj)




