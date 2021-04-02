import re
a=input()
m=re.search(r'[A-Z]',a)
n=re.search(r'[a-z]',a)
b=re.search(r'[0-9]',a)
v=re.search(r'_\S',a)
if m and n and b and v:
    print("FAM!")
else: print("NM!")