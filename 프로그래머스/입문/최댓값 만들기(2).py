def solution(numbers):
    numbers.sort()
    max1 = numbers[-1] * numbers[-2]
    max2 = numbers[0] * numbers[1]

    return max(max1, max2)