import re
s=input()
k=input()
pattern=re.compile(k)
m=pattern.search(s)
if m==None:
    print('(-1, -1)')
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = pattern.search(s,m.start() + 1)
    if m !=None:
        print(m)
