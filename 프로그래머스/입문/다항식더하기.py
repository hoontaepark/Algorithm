def solution(polynomial):
    terms = polynomial.split(" + ")  
    x_sum, num_sum = 0, 0 

    for term in terms:
        if "x" in term:
            coefficient = term.replace("x", "")  
            x_sum += int(coefficient) if coefficient else 1  
        else:
            num_sum += int(term)  


    result = []
    if x_sum:
        result.append(f"{x_sum}x" if x_sum != 1 else "x")  
    if num_sum:
        result.append(str(num_sum))  

    return " + ".join(result) 