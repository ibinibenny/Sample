int_list=[12,45,60]
str_list=['bini']
float_list=[3.5,6.8]

def var_arglist(*val):
	for item in val:
		if isinstance(item,str)==True:
			str_list.append(item)
		elif isinstance(item,int)==True:
			int_list.append(item)
		else:
			float_list.append(item)
print("list of integers:",int_list)
print("list of strings:",str_list)
print("list of float values:",float_list)

var_arglist()