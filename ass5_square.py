#5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default
class Shape:
	def area(self,area=0):
		self.area=area
		print(self.area)	
class Square(Shape):
	def __init__(self,leng):
		self.leng=leng
	def area(self):
		self.area=self.leng**2
		print(self.area)
sh=Shape()
sh.area(5)
sq=Square(int(input("length: ")))
sq.area()

