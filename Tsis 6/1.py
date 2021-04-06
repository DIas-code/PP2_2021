def maxi(a,b,c):
    mx=a
    if mx<b:
        mx=b
    if mx<c:
        mx=c
    return mx
a,b,c=int(input()),int(input()),int(input())
print(maxi(a,b,c))