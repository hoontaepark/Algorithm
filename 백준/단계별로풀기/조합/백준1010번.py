import sys
n = int(sys.stdin.readline())

for i in range(n):
    w, e = map(int, sys.stdin.readline().split())
    bridge = [[0 for _ in range(e+1)]for _ in range(w+1)]
    for j in range(1,w+1):
        for k in range(1,e+1):
            if j == 1:
                bridge[j][k] = k
                continue
            elif k == j:
                bridge[j][k] = 1
            else:
                if k > j:
                    bridge[j][k] = bridge[j][k-1] + bridge[j-1][k-1]

    print(bridge[w][e])