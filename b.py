 class Demo:
	num1=3
	
	def __init__(self,num2):
		num1=2
		self.num2=num2
		sum1=num1+self.num2
		print("the sum using instance variable: ",sum1)

	def sumnum(self,num2):
		sum1=Demo.num1+self.num2
		print("the sum using class variable: ",sum1)


obj=Demo(5)
obj.sumnum(5)
