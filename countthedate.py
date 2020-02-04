def caldate(d,m,y,num):
    import datetime
    timestart=datetime.datetime(y,m,d)
    timenum=datetime.timedelta(days=num)
    result=timestart+timenum
    print('Sau '+ str(n)+' sẽ là ngày '+str(result.day)+'/'+str(result.month)+'/'+str(result.year))
def countday(d,m,y,d2,m2,y2):
    import datetime
    oneday=datetime.timedelta(days=1)
    day=datetime.datetime(y,m,d)
    while day!=datetime.datetime(y2,m2,d2):
        result=day+oneday
        print(str(result.day)+'/'+str(result.month)+'/'+str(result.year))
        day=datetime.datetime(int(result.year),int(result.month),int(result.day))
print('NGÀY-THÁNG-NĂM')
print('Nhập ngày-tháng-năm:')
d,m,y=list(map(int,input().strip().split()))
print('1.+ ngày')
print('2. đếm ngày')
print('3. Chuyển định dạng ngày tháng năm thông qua pyperclip')
x=input()
if x=='1':
    print('Nhập số ngày cần tính:')
    n=int(input())
    caldate(d,m,y,n)
elif x=='2':
    print('Nhập ngày-tháng-năm:')
    d2,m2,y2=list(map(int,input().strip().split()))
    countday(d,m,y,d2,m2,y2)
elif x=='3':
    import re
    day=re.compile(r'(\d{2})')
    print('Sao chép 1 số vào clipboard')
