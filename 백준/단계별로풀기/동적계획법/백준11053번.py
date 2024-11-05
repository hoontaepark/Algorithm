import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
max_minus = 0
num_list_index = 0

for i in range(len(num_list) - 1):
    minus = num_list[i + 1] - num_list[i]
    if minus > max_minus:
        max_minus = minus
        num_list_index = i + 1

print(num_list_index)g