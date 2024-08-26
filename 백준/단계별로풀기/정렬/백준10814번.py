n = int(input())
user = []

for i in range(n):
    age,name = input().split()
    user.append((age, name))

user.sort(key=lambda x: int(x[0]))

for age, name in user:
    print(age,name)