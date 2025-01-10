def solution(box, n):
    count_x = box[0] // n
    count_y = box[1] // n
    count_z = box[2] // n

    return count_x * count_y * count_z