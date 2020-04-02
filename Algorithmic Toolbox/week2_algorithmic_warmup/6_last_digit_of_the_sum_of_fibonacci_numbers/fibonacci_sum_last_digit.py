# Uses python3
def calc_fib(n):
    pisano = 60
    if n < 2: return n
    n %= pisano
    fib_arr = [1,1]
    for _ in range(n):
        fib_arr.append((fib_arr[-1] + fib_arr[-2]) % 10)
    return (fib_arr[-1] - 1) % 10

n = int(input())
print(calc_fib(n))
