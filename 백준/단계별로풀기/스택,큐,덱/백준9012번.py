n = int(input())

for i in range(n):
    stack = []
    op = input()
    for j in op:
        if j == '(':
            stack.append(j)
        elif j ==')':
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break

    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")