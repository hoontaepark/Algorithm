import sys

li_1 = sys.stdin.readline().split()
li_2 = sys.stdin.readline().split()

lcs = [[0] * (len(li_2) + 1) for _ in range(len(li_1) + 1)]

for i in range(1, len(li_1) + 1):
    for j in range(1, len(li_2) + 1):
        if li_1[i - 1] == li_2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])


print(max(map(max, lcs)))