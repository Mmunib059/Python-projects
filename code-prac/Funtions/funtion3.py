# WAF to find the factorial of n. (n is the parameter)


def find_fac(a,b):
    for i in range(1, a+1):
        b *= i
    print(b)

find_fac(6,1)        