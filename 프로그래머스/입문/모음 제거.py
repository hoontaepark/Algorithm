def solution(my_string):
    collection = ("a,e,i,o,u")
    answer = ''
    for i in my_string:
        if i not in collection:
            answer += i
    return answer