real1=int(input("enter real part1"))
img1=int(input("enter img part1"))
num1=complex(real1,img1)
real2=int(input("enter real part2"))
img1=int(input("enter img part1"))
num2=complex(real1,img1)

print("--------COMPLEX CALC.----------")
operation=int(input("1.ADD\n2.SUB\n3.MUL\n4.DIV"))
if operation==1:
	print(num1+num2)
if operation==2:
	print(num1-num2)
if operation==3:
	print(num1*num2)
if operation==4:
	print(num1/num2)
