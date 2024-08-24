numberlist = []

for i in range(5):
    numberlist.append(int(input()))

sum_numberlist = sum(numberlist)

print(int(sum_numberlist / 5))
print(sorted(numberlist)[2])