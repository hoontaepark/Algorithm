alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
n = input()

for i in alphabet :
    n = n.replace(i,'0')

print(len(n))

