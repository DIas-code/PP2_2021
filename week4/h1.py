import re
n=int(input())
for i in range(n):
    a=input()
    b=re.search(r"^([-\+])?[0-9]*\.[0-9]+$",a)
    if b:
        print(True)
    else: print(False)