import time, openpyxl
#stopwatch.py
def converttime(sec):
    min=sec//60
    sec=sec%60
    hour=min//60
    min=min%60
    print('{0}:{1}:{2}'.format(int(hour),int(min),sec))
print('Welcome to the stopwatch connecting to excel file: ')
# xử lý thông tin nhập
wb=openpyxl.load_workbook('participant.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
partiinfo={}
for i in range(0,sheet.max_row):
    if i-5<0:
        break
    else:
        for z in range(0,6):
            
        