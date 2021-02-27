import time
time_test=time.strftime('%Y-%m-%d %H:%M:%S%z', time.localtime())
print (time_test)
test=time.strptime(time_test, '%Y-%m-%d %H:%M:%S%z')
print (time.strftime('%Y-%m-%d %H:%M:%S', test))
l1,l2=[],['yr','mnth','day','hr','min','sec','wkday','yrday','aaa']
for i in time.localtime():
	l1.append(i)
l3=list(zip(l2,l1))
print(l3)

