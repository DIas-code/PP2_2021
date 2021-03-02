b=list(map(int,input().split()))
cnt=1
ans,i=0,0
while i<len(b):
    if i+1<len(b) and b[i]==b[i+1]:
        cnt+=1
        i+=1
        continue
    if cnt>=3:
        ans+=cnt
        del b[i-cnt+1:i+1]
        cnt=1
        i=0
    else:
        cnt=1
        i+=1
print(ans)