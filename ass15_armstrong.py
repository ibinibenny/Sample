num=input("enter a num: ")
sumn=0
numb=num
leng=len(num)
for i in range(leng):
	sumn+=(int(num[i]))**leng
if int(numb)==sumn:
	print("yes")
else:
	print("no")




