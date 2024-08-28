n, m = map(int, input().split())
s = []
result = 0

for i in range(n):
    s.append(input())

for j in range(m):
    test = input()
    if test in s:
        result += 1

print(result)