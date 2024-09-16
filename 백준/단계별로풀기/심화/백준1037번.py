import sys
n = int(sys.stdin.readline())
number_list = list(map(int,sys.stdin.readline().split()))

max_num = max(number_list)
min_num = min(number_list)

print(max_num * min_num)