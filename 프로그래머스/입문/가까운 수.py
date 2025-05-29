def solution(array, n):
    answer = array[0]
    min_diff = abs(n - array[0])

    for i in array[1:]:
        diff = abs(n - i)
        if diff < min_diff:
            min_diff = diff
            answer = i
        elif diff == min_diff and i < answer:
            answer = i

    return answer