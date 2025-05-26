def solution(n):
    i = 1
    factorial = 1

    while True:
        if factorial > n:
            return i - 1
        i += 1
        factorial *= i