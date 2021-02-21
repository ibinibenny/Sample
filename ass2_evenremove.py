#Write a Python program to print the numbers of a specified list after removing even numbers from it. 
l1=[]
for i in range(7):
	l1.append(int(input("enter elemnt: ")))
print(l1)
for i in l1:
	print(i)
	if i%2==0:
		l1.remove(i)
print(l1)
