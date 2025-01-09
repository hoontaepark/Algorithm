def solution(my_string, n):
    answer = ''  # 결과를 저장할 빈 문자열
    for i in my_string:
        answer += i * n  # 각 문자를 n번 반복하고 answer에 추가
    return answer