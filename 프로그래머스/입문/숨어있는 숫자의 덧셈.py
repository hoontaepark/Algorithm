def solution(my_string):
    answer = 0
    number = ['0','1','2','3','4','5','6','7','8','9']
    for i in my_string:
        if i in number:
             answer += int(i)
    return answer