
def rmvpunct(str1):
	str2=str1.replace('.',' ')
	str2=str2.replace(',',' ')
	str2=str2.replace('(',' ')
	str2=str2.replace(')',' ')
	return str2

print(rmvpunct(input("enter a multisentence string")))
