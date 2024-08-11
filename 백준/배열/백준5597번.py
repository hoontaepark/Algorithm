student = [i for i in range(1,31)]

for j in range(28):
    a = int(input())
    student.remove(a)

print(min(student))
print(max(student))