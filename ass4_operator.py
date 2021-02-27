#4. Write a program to implement operator module ?
import operator
print(operator.add(3,4))
print(operator.sub(5,2))
print(operator.mul(9,3))
print(operator.truediv(20,6))
print(operator.floordiv(20,6))
lis=[4,6,7,8]
it=operator.getitem(lis,1)
print(it)
it=operator.setitem(lis,1,8)
print(lis)
print(operator.neg(6))
print(operator.gt(6,3))
print(operator.pow(2,4))
operator.delitem(lis,2)
print(lis)


