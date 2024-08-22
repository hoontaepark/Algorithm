rectangle = list(map(int, input().split()))
rectangle.sort()

if rectangle[0] + rectangle[1] > rectangle[2]:
    print(sum(rectangle))
else:
    print((rectangle[0] + rectangle[1]) * 2 -1)