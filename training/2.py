import re
txt = input()
a=input()
pattern=re.compile(a)
m=pattern.search(txt)
if m:
    print("First time Polinoma occured in position:", m.start())
else: print("Not found")