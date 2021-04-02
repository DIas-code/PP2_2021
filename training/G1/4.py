n=int(input())
a=input()
s=""
for i in range (0,len(a)):
    c=a[i]
    v=ord(c)+n
    if v>90:
        s+=chr(v-26)
    else:s+=chr(v)
print(s)