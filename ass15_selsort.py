#15. Program to implement Selection-Sort Algorithm.
def list_read(lis):
	#def to read a list
	lim=int(input('lim?'))
	for i in range(lim):
		elem=int(input("elem?"))
		l1.append(elem)

def selsort(l2,k=0):
	#def for selection sort
	print(l2)
	if l2!=sorted(l2):
		rep_avd=l2[k:]
		print(rep_avd)
		small=min(rep_avd)
		sm_in=rep_avd.index(small)+k
		if l2[k]!=small:
			tmp=l2[k]
			l2[k]=small
			l2[sm_in]=tmp
		k+=1
		selsort(l2,k)
l1=[]
list_read(l1)
print(l1)

selsort(l1)
print("sorted list=",l1)


