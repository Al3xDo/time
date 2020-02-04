import re,pyperclip
dayf=re.compile(r"""
^(.*?)?
((0|1|2|3)?\d)
(-|/|.)
((0|1)?\d)
(-|/|.)
(\d{4})
(.*?)?$
""",re.VERBOSE)
time=pyperclip.paste()
retime=dayf.search(time)
text=retime.group(1)
day=int(retime.group(2))
mon=int(retime.group(5))
yea=int(retime.group(8))
aftertext=retime.group(9)
print(day,mon,yea)