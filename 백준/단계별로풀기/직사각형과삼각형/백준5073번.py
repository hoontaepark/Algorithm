while True:
    a,b,c = map(int, input().split())
    if a == 0:
        break
    square_max = max(a,b,c)
    if a + b + c - square_max <= square_max:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")