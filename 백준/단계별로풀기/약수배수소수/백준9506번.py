while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    n_list = []
    for i in range(1, n):
        if n % i == 0:
            n_list.append(i)
    if sum(n_list) == n:
        print(n, " = ", " + ".join(str(i) for i in n_list), sep="")
    else:
        print(n, "is NOT perfect.")