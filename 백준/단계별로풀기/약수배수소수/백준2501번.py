a,b = map(int,input().split())
a_list = []

for i in range(1, a+1):
    if a % i == 0:
        a_list.append(i)

if len(a_list) < b:
    print(0)
else:
    print(a_list[b-1])