def solution(order):

    str_order = str(order)
    str_num = ["3","6","9"]
    count = 0

    for i in str_order:
        if i in str_num:
            count += 1

    return count
