n, m = map(int, input().split())

n_list = [i for i in range(1, n+1)]
temp = 0

for j in range(m):
    a, b = map(int, input().split())
    temp = n_list[a-1]
    n_list[a-1] = n_list[b-1]
    n_list[b-1] = temp

for k in range(n):
    print(n_list[k], end=" ")