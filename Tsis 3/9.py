n=int(input())
a=list(map(int,input().split()))
mx=a[0]
for i in range (1,len(a)):
    if mx<a[i]:
        mx=a[i]
print(mx)