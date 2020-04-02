# Uses python3
def gcd_naive(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
