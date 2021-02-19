#to print all prime no.s within a limit

lim=int(input("enter limit"))
flag=0
for i in range(3,lim):
	for j in range(2,i):
		if i%j==0:
			
			break
		else:
			flag=0
	if flag==0:
		print(i)		
			

