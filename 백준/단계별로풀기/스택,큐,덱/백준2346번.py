import sys
from collections import deque
n = int(sys.stdin.readline())

queue = deque(enumerate(map(int, sys.stdin.readline().split())))

answer = []

while queue:
    idx, now_turn = queue.popleft()
    answer.append(idx + 1)

    if now_turn > 0:
        queue.rotate(-(now_turn - 1))
    elif now_turn < 0:
        queue.rotate(-now_turn)

print(' '.join(map(str, answer)))