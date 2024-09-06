def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

n = int(input())
arr = []
distance = []
for i in range(n):
    arr.append(int(input()))
    if i != 0:
        distance.append(arr[i]-arr[i-1])

max_gcd = distance[0]
for i in range(n-2):
    max_gcd = gcd(distance[i+1]-distance[i], max_gcd)

result = ((arr[n-1]-arr[0])//max_gcd - 1) - n + 2
print(result)