import re
a=input()
m=re.search(r'[A-Z]{1}[a-z]{1}',a)
if m:
    print("FAM!")
else: print("NM!")