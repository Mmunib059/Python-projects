def mun(n):
    if n == 0:
        return
    print(n)
    mun(n-1)
    
# mun(5) 

def fac(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fac(n-1)
print(fac(6))
# fac(n)