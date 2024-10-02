import sys
n = int(sys.stdin.readline())

def dfs(start):
    global cnt

    if start == n:
        cnt += 1
    else:
        for i in range(n):
            if not cols[i] and not diag1[start + i] and not diag2[start - i + n - 1]:
                cols[i] = diag1[start + i] = diag2[start - i + n - 1] = True
                dfs(start + 1)

                cols[i] = diag1[start + i] = diag2[start - i + n - 1] = False

cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
cnt = 0
dfs(0)

print(cnt)