def convert_to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n //= base
    return result

n, m = input().split()
n = int(n)
m = int(m)

result = convert_to_base(n, m)
print(result)
