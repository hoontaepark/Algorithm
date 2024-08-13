a,b = map(int, input().split())

n_list = list(map(int, input().split()))

for i in range(a):
    if n_list[i] < b :
        print(n_list[i], end=" ")