import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    op = sys.stdin.readline().split()
    if op[0] == '1':
        stack.append(int(op[-1]))
    elif op[0] == '2':
        if stack:
            print(stack.pop(-1))
            continue
        print(-1)
    elif op[0] == '3':
        print(len(stack))
    elif op[0] == '4':
        if stack:
            print(0)
            continue
        print(1)
    elif op[0] == '5':
        if stack:
            print(stack[-1])
            continue
        print(-1)



