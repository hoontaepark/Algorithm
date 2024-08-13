n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum_score = 0

for i in range(n):
    score[i] = score[i]/max_score*100

for j in range(n):
    sum_score += score[j]

print(sum_score/n)
