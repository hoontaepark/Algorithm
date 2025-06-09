def solution(s):
     answer = []

     for i in s:
         if i == "Z":
             if i:
                 answer.pop()
         else:
             answer.append(int(i))

     return sum(answer)