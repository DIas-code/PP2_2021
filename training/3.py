n=int(input())
l=list(map(int,input().split()))
s=set(l)
if len(s)==len(l):
    print("YES")
else: print ("NO")
