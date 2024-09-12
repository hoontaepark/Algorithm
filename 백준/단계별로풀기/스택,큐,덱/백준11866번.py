import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
yosep = []

queue = deque([i for i in range(1, n+1)])

while queue:
    for j in range(k-1):
        queue.append(queue.popleft())
    yosep.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, yosep)), end="")
print(">")
