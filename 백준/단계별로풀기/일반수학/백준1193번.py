n = int(input())
m = 1

while n > m:
    n -= m
    m += 1

if m % 2 == 0:
    a = n
    b = m - n + 1
if m % 2 == 1:
    a = m - n + 1
    b = n

print(f'{a}/{b}')
