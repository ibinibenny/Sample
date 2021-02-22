

# open the sample file used 
file = open('file1.txt') 
  
# read the content of the file opened 
content = file.readlines() 
  
# read 10th line from the file 
print("tenth line:") 
print(content[-1]) 
  
# print first 3 lines of file 
print("first three lines:") 
print(content[0:7]) 
