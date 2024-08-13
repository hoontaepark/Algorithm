n = int(input())

for i in range(n):
    r, word = input().split()
    r = int(r)
    result = ""

    for j in word:
        result += j * r

    print(result)