import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

price_min = price[0]
total = 0

for i in range(n-1):

    if price_min > price[i]:
        price_min = price[i]

    total += (price_min * distance[i])

print(total)