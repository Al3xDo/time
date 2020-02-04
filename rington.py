import datetime,time
timeleft=3
while timeleft >0:
    print(timeleft)
    time.sleep(1)
    timeleft=timeleft-1
if timeleft==0:
    import subprocess
    subprocess.Popen(['start','guests.txt'],shell=True)
