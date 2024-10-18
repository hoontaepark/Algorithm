import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

d = [0]*n
d[0] = lst[0]
for i in range(1,n):
    d[i] = max(lst[i],d[i-1]+lst[i])

print(max(d))