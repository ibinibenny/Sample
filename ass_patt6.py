j=1
lines=int(input("enter no.of lines"))
for i in range(lines,0,-1):
	print(' '*i,end=' ')
	print('# '*j,end='   '*j)
	print("\n")
	j+=1
