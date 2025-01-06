def solution(n, k):
    free_drinks = n // 10

    paid_drinks = k - free_drinks

    total_cost = (n * 12000) + (max(paid_drinks, 0) * 2000)

    return total_cost