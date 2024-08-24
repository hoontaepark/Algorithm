n = int(input())
xy_list = []

for i in range(n):
    [x,y] = map(int,input().split())
    xy_list.append([x,y])

xy_list.sort()

for j in range(n):
    print(xy_list[j][0],xy_list[j][1])