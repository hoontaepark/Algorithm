n = int(input())

x_list = []
y_list = []

for i in range(n):
    x,y=map(int,input().split())
    x_list.append(x)
    y_list.append(y)

x_listmax = max(x_list)
x_listmin = min(x_list)
y_listmax = max(y_list)
y_listmin = min(y_list)


print((x_listmax-x_listmin)*(y_listmax-y_listmin))