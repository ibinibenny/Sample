class Bank:
	min_bal=500
	acc_tab={}
	

	def __init__(self,name,acc_no):
		self.name=name
		self.acc_no=acc_no
		self.curr_bal=Bank.min_bal
		Bank.acc_tab[self.acc_no]=self.curr_bal

	def deposit(self,acc_no,dep_amt):
		Bank.acc_tab[acc_no]+=dep_amt

	def withdraw(self,acc_no,withdraw_amt):
		if Bank.acc_tab[acc_no]>Bank.min_bal:
			Bank.acc_tab[acc_no]-=withdraw_amt

		else: print("sorry!need to maintain above min.balance for withdrawl!!")

	def display(self):
		print("____________________________\n")
		name=self.name
		print("Name:            ",name.title())
		print("Account number:  ",self.acc_no)
		print("current balance: ",Bank.acc_tab[self.acc_no])
		print("____________________________")


dictt,l1={},[]
i,acc_hldr=0,0
while i<10:
	print("\n\n......Steps Bank.......")
	opt=int(input("1.create an account\n2.deposit\n3.withdraw\n"))
	if opt==1:
		acc=623400
		name=input("Enter ur Name: ")
		acc_hldr+=1
		acc+=acc_hldr
		obj=Bank(name,acc)
		l1=[name,obj]
		dictt[acc]=l1
		obj.display()
	
	elif opt==2:
		acc_num=int(input("enter Account Number: "))
		dep_amt=int(input("enter deposit amnt: "))
		l2=dictt[acc_num]
		l2[1].deposit(acc_num,dep_amt)
		l2[1].display()

	elif opt==3:
		acc_num=int(input("enter Account Number:"))
		withdraw_amt=int(input("enter withdraw amnt: "))
		l2=dictt[acc_num]
		l2[1].withdraw(acc_num,withdraw_amt)
		l2[1].display()
	
	else:
		print("wrong opt!!")
	i+=1




	
	
