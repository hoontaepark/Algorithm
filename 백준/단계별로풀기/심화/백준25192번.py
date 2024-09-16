n = int(input())
gomgom = set()
count = 0

for i in range(n):
    user = input().strip()
    if user == 'ENTER':
        count += len(gomgom)
        gomgom = set()
    else:
        gomgom.add(user)

count += len(gomgom)
print(count)