n = int(input())
m = int(input())
nm_list = []

for i in range(n,m+1):
    count = 0
    if i>1:
        for j in range(2,i):
            if i%j == 0:

                count += 1
                break
        if count == 0:
            nm_list.append(i)

if len(nm_list)<1:
    print(-1)
else:
    print(sum(nm_list))
    print(min(nm_list))
