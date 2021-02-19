n = int(input())
a = list(map(int, input().split()))
print(a[n-1],*a[0:n-1])