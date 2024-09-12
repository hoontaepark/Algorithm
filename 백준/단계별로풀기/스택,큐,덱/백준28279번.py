import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        queue.appendleft(command[1])
    elif command[0] == '2':
        queue.append(command[1])
    elif command[0] == '3':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == '4':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == '5':
        print(len(queue))
    elif command[0] == '6':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == '7':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == '8':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])




