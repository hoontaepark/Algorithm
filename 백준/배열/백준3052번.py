count = 0
n_list = []

for i in range(10):
    n = int(input()) % 42
    n_list.append(n)

#중복값 제거
outboth = set(n_list)
count = len(outboth)

print(count)