#Write a program to take a string as input and return a string with vowels removed.(implement List Comprehesion)
str1,st=input("enter string: "),' '
vow=['a','e','i','o','u','A','E','I','O','U']
def vowremv(str2):
	st=' '
	vowremvd=[i for i in str2 if i not in vow]
	for i in vowremvd:
		st+=i
	return st
print(list(vowremv(str1)))
