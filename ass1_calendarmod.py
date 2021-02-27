#1. Programs to implement the concept of calendar module.
import calendar
ob=calendar.TextCalendar(calendar.MONDAY)
ob.prmonth(2012,12)
for i in calendar.month_name:
	print(i)
print("\n",calendar.month_name[4])
print("\n",calendar.day_name[3])
for i in calendar.day_name:
	print(i)
day=input("enter a day:")
print(list(calendar.day_name).index(day.title()))
month=input("enter month: ")
print(list(calendar.month_name).index(month.title()))
mnth=list(calendar.month_name).index(month.title())
yr=int(input("year:"))
ob.prmonth(yr,mnth)
print(ob.formatmonth(2006,1))


