from collections import Counter
n = int(input())
havecard = list(map(int,input().split()))
m = int(input())
hascard = list(map(int,input().split()))
result = []

dic = Counter(havecard)

for i in hascard:
    if i in dic:
        result.append(1)
    else:
        result.append(0)

print(*result)
