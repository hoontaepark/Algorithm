def solution(age):
    num_to_alpha = {str(i): chr(ord('a') + i) for i in range(10)}
    return ''.join(num_to_alpha[digit] for digit in str(age))