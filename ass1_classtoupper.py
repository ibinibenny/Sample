class ToUpper:
	#a class which has  two methods one, to get a string from console  input and other is to print the string in uppercase.
	def __init__(self,str1):
		self.str1=str1
		print(self.str1)
	def upper(self,str1):
		str2=self.str1
		str2=str2.upper()
		print(str2)
st=input("enter a string:")
obj=ToUpper(st)
obj.upper(st)
