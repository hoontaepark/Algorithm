n = int(input())

changes = [25, 10, 5, 1]
for i in range(n):
    money = int(input())
    result = []

    for j in changes:
        result.append(money // j)
        money = money % j

    print(*result)