n = int(input())
havecard = list(map(int,input().split()))
m = int(input())
hascard = list(map(int,input().split()))

count = {}

for i in havecard:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

for j in hascard:
    result = count.get(j)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
