dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = input()
count = 0
for i in range(len(n)):
    for j in dial:
        if n[i] in j:
            count += dial.index(j)+3
print(count)
