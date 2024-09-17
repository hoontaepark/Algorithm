import sys
n = int(sys.stdin.readline())
number_list = []

for i in range(n):
    number_list.append(int(sys.stdin.readline()))

number_list.sort()

print(round(sum(number_list)/len(number_list)))
print(number_list[len(number_list)//2])

dic = dict()
for j in number_list:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1

max_num = max(dic.values())
max_dic = []

for k in dic:
    if max_num == dic[k]:
        max_dic.append(k)

if len(max_dic)>1:
    print(max_dic[1])
else:
    print(max_dic[0])


print(max(number_list)-min(number_list))