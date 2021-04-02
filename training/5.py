n=int(input())
st=list(map(str,input().split()))
m=int(input())
cst=list(map(str,input().split()))
print("Missed students:")
for i in st:
    if i in cst:
        continue
    else: print("-", i)
print("Not in the group:")
for i in cst:
    if i in st:
        continue
    else: print("-", i)
