x = int(input())
n = int(input())

sum = 0
for i in range(n):
    item, count = map(int, input().split())
    total = item * count
    sum += (total)

if x == sum:
    print("Yes")
else:
    print("No")