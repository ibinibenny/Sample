
punctuation='''''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
a=input("enter a string:")
b=""
for i in a:
	if i not in punctuation:
		b=b+i
print("string without punctuation",b)
