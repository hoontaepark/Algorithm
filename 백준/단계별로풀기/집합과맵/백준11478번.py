a = input()
count = set()

for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        count.add(a[i:j])

print(len(count))