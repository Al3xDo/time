import datetime,time
from datetime import date
today=date.today()
day=today.day
mon=today.month
yea=today.year
now=datetime.datetime(yea,mon,day)
PigBday=datetime.datetime(yea,2,21)
myBday=datetime.datetime(yea,2,7)
if now>PigBday:
    PigBday=datetime.datetime(yea+1,2,21)
    reday=PigBday-now
    redayM=myBday-now
    print('còn '+str(reday)+' là tới sinh nhật heo mập <3')
    print('còn '+str(redayM)+' là tới sinh nhật bò sữa <3')
else:
    reday=PigBday-now
    redayM=myBday-now
    print('còn '+str(reday)+' là tới sinh nhật heo mập <3')
    print('còn '+str(redayM)+' là tới sinh nhật bò sữa <3')

