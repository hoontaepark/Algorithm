import sys
from collections import deque

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
list_c = list(map(int, sys.stdin.readline().split()))

queue = deque()

for i in range(n):
    if list_a[i] == 0:
        queue.appendleft(list_b[i])

for j in range(m):
    queue.append(list_c[j])
    print(queue.popleft(), end=' ')

