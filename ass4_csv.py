#Write a program to perform read and write operation on a CSV File ?
import csv
fp=open('db.csv',"w+")
f=csv.writer(fp)
f.writerow(["Name","Place","Age"])
f.writerows([("k","toronto",22),("B","VanCouver",45),("c","yemen",34)])
fp.close()
fg=open("db.csv","r")
g=csv.reader(fg)
for i in g:
	print(i)
