n,m = map(int,input().split())
poketmon = {}

for i in range(1, n+1):
    name = input()
    poketmon[i] = name
    poketmon[name] = i


for j in range(m):
    name = input()
    if name.isdigit():
        print(poketmon[int(name)])
    else:
        print(poketmon[name])