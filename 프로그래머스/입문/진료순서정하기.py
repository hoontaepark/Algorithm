def solution(emergency):
    answer=[]
    dic = {}
    sorted_emergency = sorted(emergency, reverse=True)
    for idx, val in enumerate(sorted_emergency, start=1):
        dic[val] = idx
    for i in emergency:
        answer.append(dic.get(i))
    return answer