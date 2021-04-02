import re
txt=input()
t=input()
s=input()
txt=txt.replace(t,s)
f=input()
pat=re.compile(f)
m=pat.findall(txt)
print(len(m))