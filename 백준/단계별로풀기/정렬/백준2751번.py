import sys
n = int(input())
n_list = []

for i in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

for j in n_list:
    print(j)


