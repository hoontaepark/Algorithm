n = int(input())
stack = []

for i in range(n):
    op = int(input())
    if op == 0:
        stack.pop(-1)
    else:
        stack.append(op)

print(sum(stack))