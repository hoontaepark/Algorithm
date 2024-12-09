import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

prefix_sum = 0
remainder_count = [0] * m
remainder_count[0] = 1
count = 0

for i in range(n):
    prefix_sum += num[i]
    remainder = prefix_sum % m

    if remainder < 0:
        remainder += m

    count += remainder_count[remainder]
    remainder_count[remainder] += 1

print(count)

