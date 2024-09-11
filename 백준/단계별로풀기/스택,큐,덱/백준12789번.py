n = int(input())

student = list(map(int,input().split()))
stack = []

m = 1
for i in student:
    stack.append(i)
    while stack and stack[-1] == m:
        stack.pop()
        m += 1

if stack:
    print('Sad')
else:
    print('Nice')

