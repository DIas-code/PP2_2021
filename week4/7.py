n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range (0,len(a)-1,2):
    b.append(a[i+1])
    b.append(a[i])
if n%2==1:    
    b.append(a[n-1])
print(*b)