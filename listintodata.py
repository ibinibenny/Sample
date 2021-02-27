int_list=[]
str_list=[]
float_lst=[]

def var_arglist(*val):
	for item in val:
		if isinstance(item,str)==True:
			str_list.append(item)
		elif isinstance(item,int)==True:
			int_list.append(item)
		else:
			float_lst.append(item)
print("list of integers:",int_list)
print("list of strings:".str_list)
print("list of float values:",float_list)

var_arglist(10,20,30,'anu',50,75,'ajo')