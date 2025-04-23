def solution(n):
    def count_divisors(x):
        cnt = 0
        for i in range(1, x + 1):
            if x % i == 0:
                cnt += 1
        return cnt

    answer = 0
    for i in range(1, n + 1):
        if count_divisors(i) >= 3:
            answer += 1
    return answer
