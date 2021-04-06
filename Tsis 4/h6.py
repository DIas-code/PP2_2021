# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
while n>0:
    a=input()
    
    m=re.search(r'[A-Za-z]+ <[A-Za-z](\w|_|\.|-)+@[a-z]+\.[a-z]{1,3}>',a)
    if m:
        print(a) 
    n-=1
"""4
this <is@valid.com>
this <is_som@radom.stuff>
this <is_it@valid.com>
this <_is@notvalid.com>"""