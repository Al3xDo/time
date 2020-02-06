import time,pyperclip
def convert(stime,info):
    etime=time.time()-stime
    retime=round(etime,2)
    info.append(retime)
print('Enter to start:')
x=input()
startt=time.time()
print('Enter to record time or space to exit program:')
x=input()
info=[]
info.append(0)
while True:
    if x=='':
        convert(startt,info)
        x=input()
    elif x==' ':
        body=''
        for i in range(1,len(info)):
            body=body+'Lap #'+str(i+1).rjust(2,' ')+':'.ljust(3,' ')+str(info[i]).rjust(5,' ')+' ( '+str(round(info[i]-info[i-1],2)).rjust(5,' ')+')\n'
            print('Lap #'+str(i+1).rjust(2,' ')+':'.ljust(3,' ')+str(info[i]).rjust(5,' ')+' ( '+str(round(info[i]-info[i-1],2)).rjust(5,' ')+')')
        pyperclip.copy(body)
        print('Exited')
        break
