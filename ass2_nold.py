#Write a program that accepts a sentence and calculate the number of letters & digits
str1=input("enter string")
let,dig,oth=0,0,0
for i in str1:
	if i.isalpha():
		let+=1
	elif i.isalnum():
		dig+=1
	else:
		oth+=1
print("letter count=",let,"\ndigit count=",dig,"\nothers=",oth)
