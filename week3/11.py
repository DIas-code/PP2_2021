n=int(input())
a=list(map(int,input().split()))
b=int(input())
place=1
for i in range (0,len(a)):
    if b<=a[i]:
        place+=1
print(place)