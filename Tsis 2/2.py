n=list(map(int,input().split()))
a=1001
for i in range(0, len(n)):
    if n[i]>0 and a>n[i]:
        a=n[i]
print(a)