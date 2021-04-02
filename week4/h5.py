# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
while n>0:
    a=input()
    if len(a)==10:
        m=re.search(r'[789][0-9]{9}',a)
        if m:
            print("YES")
        else: print("NO")
    else :print("NO") 
    n-=1