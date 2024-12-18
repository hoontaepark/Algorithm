import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
people.sort()
time = 0
total_time = 0

for i in people:
    time += i
    total_time += time

print(total_time)