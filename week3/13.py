n = int(input())
a = list(map(int, input().split()))
c = int(input()) % len(a)
print(c)
print(*a[-c:], end=" ")
print(*a[0:-c])