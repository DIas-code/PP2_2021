def sum(listt):
    s=0
    for i in listt:
        s+=i
    return s
listt=list(map(int,input().split()))
print(sum(listt))