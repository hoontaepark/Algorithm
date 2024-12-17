import sys
input = sys.stdin.readline

coin = []
count = 0

n, k = map(int, input().split())

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

for value in coin:
    count += k // value
    k %= value
    if k <= 0:
        break

print(count)