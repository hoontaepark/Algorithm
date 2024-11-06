import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

reverseA = A[::-1]

inc_dp = [1] * n
dec_dp = [1] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

        if reverseA[i] > reverseA[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)


dec_dp = dec_dp[::-1]

result = []
for i in range(n):
    result.append(dec_dp[i] + inc_dp[i] - 1)

print(max(result))