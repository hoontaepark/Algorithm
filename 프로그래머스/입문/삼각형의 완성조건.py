def solution(sides):
    sides.sort()
    longest = sides[-1]
    plus = sides[0] + sides[1]
    if longest < plus:
        return 1
    else:
        return 2
