n=int(input())
m=set(map(int,input().split()))
l=[]
for i in m:
    l.append(i)
print(m)
print(l)
a=1
for i in sorted(l):
    print(a, i)
    a+=1
