# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        print(0)
        return [1]
    ops = min_ops(n)
    return construct_min_list(n, ops)

def construct_min_list(n, ops):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0: 
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0: 
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return reversed(sequence)

def min_ops(n):
    result = [0]*(n+1)
    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 2 == 0:
            min2 = result[i//2]
        if i % 3 == 0:
            min3 = result[i//3]
        minOp = min(min1, min2, min3)

        result[i] = minOp + 1
    print(result[n])
    return result


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(*sequence)