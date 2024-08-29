a,b = map(int,input().split())
a_list = set(map(int,input().split()))
b_list = set(map(int,input().split()))

a_list_minus = []
b_list_minus = []

for i in a_list:
    if i not in b_list:
        a_list_minus.append(i)

for j in b_list:
    if j not in a_list:
        b_list_minus.append(j)

print(len(a_list_minus)+len(b_list_minus))
