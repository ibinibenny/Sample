#largest among 3 no.s

num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1>num2:
	if num1>num3:
		print(num1,"is the largest")
	else:
		print(num3,"is the largest")
else:
	if num2>num3:
		print(num2,"is the largest")
	else:
		print(num3,"is the largest")
		
