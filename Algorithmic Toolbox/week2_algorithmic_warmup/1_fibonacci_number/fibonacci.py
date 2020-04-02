# Uses python3
def calc_fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    a = 0
    b = 1
    c = 0
    for i in range(2,n+1):
        c = a+b
        a = b
        b = c
    return c
n = int(input())
print(calc_fib(n))
