n,m = map(int, input().split())
n_list = [i for i in range(1, n+1)]

for i in range(m):
    a,b = map(int, input().split())
    #리스트 슬라이싱 a~b는 a~b까지 역순
    n_list[a-1:b] = n_list[a-1:b][::-1]

for j in range(n):
    print(n_list[j], end=" ")


