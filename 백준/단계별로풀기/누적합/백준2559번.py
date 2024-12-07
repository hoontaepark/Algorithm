import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tem = list(map(int, input().split()))

s = []
s.append(sum(tem[:m]))

for i in range(n-m):
    s.append(s[i] - tem[i] + tem[m+i])

print(max(s))