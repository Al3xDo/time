import time,pyperclip,datetime,re
dayf=re.compile(r"""
^(.*?)?
((0|1|2|3)?\d)
(-|/|.)
((0|1)?\d)
(-|/|.)
(\d{4})
(.*?)?$
""",re.VERBOSE)
while True:
    print('1. Exit')
    print('2.Transfer time')
    x=input()
    if x=='1':
        break
    if x=='2':
        print('Processing....')
        time=pyperclip.paste()
        if time==None:
            print('Error, u need to copied the time to clipboard')
        else:
            retime=dayf.search(time)
            if retime==None:
                print('Error')
            else:
                text=retime.group(1)
                day=int(retime.group(2))
                mon=int(retime.group(5))
                yea=int(retime.group(8))
                aftertext=retime.group(9)
                retimefor=datetime.datetime(yea,mon,day)
                # GUI
                print('Select your format (this will be added to clipboard):')
                print('1.American format')
                print('2.Full month name with day of the month')
                print('3.Full month name with day of the month and the week (0-6)')
                print('4.Full month name with day of the month and full weekday name')
                print('5. Abbreviated month name ....')
                print('6. Abbreviated month name ....')
                print('7. Abbreviated month name ....')
                n=input()
                global resut 
                #Processing
                if n=='1':
                    resut=text+str(mon)+'.'+str(day)+'.'+str(yea)+aftertext
                elif n=='2':
                    resut=text+retimefor.strftime('%B of %d, %Y')+aftertext
                elif n=='3':
                    resut=text+retimefor.strftime('%w, %B of %d, %Y')+aftertext
                elif n=='4':
                    resut=text+retimefor.strftime('%W, %B of %d, %Y')+aftertext
                elif n=='5':
                    resut=text+retimefor.strftime('%b of %d, %Y')+aftertext
                elif n=='6':
                    resut=text+retimefor.strftime('%w, %b of %d, %Y')+aftertext
                elif n=='7':
                    resut=text+retimefor.strftime('%W, %b of %d, %Y')+aftertext
                print(resut)
                pyperclip.copy(resut)
                print('copied to clipboard')
