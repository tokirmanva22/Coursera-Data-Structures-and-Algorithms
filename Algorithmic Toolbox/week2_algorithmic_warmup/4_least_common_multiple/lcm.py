# Uses python3
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

def lcm_naive(a, b):
    return (a*b) // gcd(a,b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

