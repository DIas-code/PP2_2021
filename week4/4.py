n=int(input())
a=list(map(int,input().split()))
b=0
for i in range (1,len(a)):
    if (a[i]>0 and a[i-1]>0) or (a[i]<0 and a[i-1]<0):
        b+=1
    
if b>0:
    print("YES")
else: print("NO")