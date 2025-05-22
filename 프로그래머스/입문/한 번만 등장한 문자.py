def solution(s):
    from collections import Counter
    count = Counter(s)

    one_time_chars = [char for char in count if count[char] == 1]


    one_time_chars.sort()

    return ''.join(one_time_chars)