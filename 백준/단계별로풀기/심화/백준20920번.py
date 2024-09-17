import sys
input = sys.stdin.readline

n, m = map(int, input().split())

voca = {}

for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in voca:
            voca[word] += 1
        else:
            voca[word] = 1



voca = sorted(voca.items(),key = lambda x: (-x[1],-len(x[0]), x[0]))

for j in voca:
    print(j[0])

