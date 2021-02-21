row_no=int(input("no.of rows?"))
col_no=int(input("no.of cols?"))
lis=[]
for i in range(col_no):
	list1=[]
	for j in range(row_no):
		elem=int(input("enter element:"))
		list1.append(elem)
	lis.append(list1)
print(lis)
'''for j in range(col_no+1):
	list2=[]
	for i in lis:
		list2.append(i[j])
	list1.append(list2)'''
list1,list2=[],[]
for i in range(row_no):
	list2=[]
	for j in range(col_no):
		list2.append(lis[j][i])
	list1.append(list2)
print(list1)
	


			
