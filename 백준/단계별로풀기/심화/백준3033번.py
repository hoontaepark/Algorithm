chess = [1,1,2,2,2,8]
havechess = list(map(int, input().split()))
count = []
chessmath = 0

for i in range (6) :
    if chess[i] < havechess[i] :
        chessmath = havechess[i] - chess[i]
        count.append(-chessmath)
    else :
        chessmath = chess[i] - havechess[i]
        count.append(chessmath)

for j in range(6):
    print(count[j], end=" ")