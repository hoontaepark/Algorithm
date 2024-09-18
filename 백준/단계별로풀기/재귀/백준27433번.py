import sys
n = int(sys.stdin.readline())
pactorial = 1

for i in range(1,n+1):
    pactorial *= i

print(pactorial)