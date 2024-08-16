n = int(input())
sum = 0
board = [[0 for _ in range(101)]for _ in range(101)]

for i in range(n):
    x,y = list(map(int,input().split()))

    for j in range(x, x+10):
        for k in range(y, y+10):
            board[j][k] = 1

for i in board:
    sum += i.count(1)

print(sum)