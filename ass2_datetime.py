#2. Write Programs to implement datetime module ?
import datetime
now=datetime.datetime.now()
print("today is:%d/%d/%d " %(now.day,now.month,now.year))
print(datetime.MINYEAR,datetime.MAXYEAR)
print("time is %d:%d:%d" %(now.hour,now.minute,now.second))

