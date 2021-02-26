#13. Write a program to implement Insertion-Sort algorithm in python.
def list_read(lis):
	#def to read a list
	lim=int(input('lim?'))
	for i in range(lim):
		elem=int(input("elem?"))
		l1.append(elem)

def insertion_sort(lis):
	#func for insertion sort
	for i in range(len(lis)):
		for j in range(i):
			if lis[i]<lis[j]:
				temp=lis[j]
				lis[j]=lis[i]
				lis[i]=temp
	return lis

l1=[]
list_read(l1)
print(insertion_sort(l1))
