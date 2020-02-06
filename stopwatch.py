import time, openpyxl
#stopwatch.py
partiinfo={}
def converttime(sec,value):
    min=sec//60
    sec=sec%60
    hour=min//60
    min=min%60
    partiinfo[value]='{0}:{1}:{2}'.format(int(hour),int(min),sec)
print('Welcome to the stopwatch connecting to excel file: ')
# xử lý thông tin nhập
wb=openpyxl.load_workbook('partiinfo.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
print('Each race will include 5 participants')
for i in range(2,sheet.max_row+1,5):
    if sheet.max_row-i<5:
        print('Last race:')
        dem=[]
        s=0
        for z in range(1,sheet.max_row-len(partiinfo)+1):
            print(str(z)+'-' + str(sheet.cell(row=i+z,column=1).value) +'-' + sheet.cell(row=i+z,column=2).value)
            tam=z+i
            dem.append(tam)
            s=s+z
        print('Enter to begin:')
        x=input()
        startime=time.time()
        sd=0
        while sd!=s:
            converttime(startime,sheet.cell(row=dem[x],column=1).value)
            sd=sd+x
            x=int(input())
    else:
        print('1-'+str(sheet.cell(row=i,column=1).value)+'-'+sheet.cell(row=i,column=2).value)
        print('2-'+str(sheet.cell(row=i+1,column=1).value)+'-'+sheet.cell(row=i+1,column=2).value)
        print('3-'+str(sheet.cell(row=i+2,column=1).value)+'-'+sheet.cell(row=i+2,column=2).value)
        print('4-'+str(sheet.cell(row=i+3,column=1).value)+'-'+sheet.cell(row=i+3,column=2).value)
        print('5-'+str(sheet.cell(row=i+4,column=1).value)+'-'+sheet.cell(row=i+4,column=2).value)
        print('Enter to begin:')
        x=input()
        startime=time.time()
        print("Enter to each number to record the participant's time (this will auto save to excel file):")
        x=int(input())
        s=0
        Ninfo=len(partiinfo)
        tong=len(partiinfo)-Ninfo
        while tong!=5:
            if x==1:
                converttime(startime,sheet.cell(row=i,column=1).value)
                s=s+x
                if tong!=5:
                    x=int(input())
            elif x==2:
                converttime(startime,sheet.cell(row=i+1,column=1).value)
                s=s+x
                if tong!=5:
                    x=int(input())
            elif x==3:
                converttime(startime,sheet.cell(row=i++2,column=1).value)
                s=s+x
                if tong!=5:
                    x=int(input())
            elif x==4:
                converttime(startime,sheet.cell(row=i+3,column=1).value)
                s=s+x
                if tong!=5:
                    x=int(input())
            elif x==5:
                converttime(startime,sheet.cell(row=i+4,column=1).value)
                s=s+x
                if tong!=5:
                    x=int(input())
        print('Race end. The information will be saved...')
# xử lý excel
for z in range(0,sheet.max_row+1):
    sheet.cell(row=z,column=3).value=partiinfo[sheet.cell(row=z,column=1).value]
#wb.save('recored.xlsx')
print('Saved')


