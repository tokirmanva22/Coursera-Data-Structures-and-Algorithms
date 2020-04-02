# Uses python3
import sys

def binary_search(a, x ,l, r):
    while l <= r:
        mid = l + (r-l)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            r = mid-1
        else:
            l = mid+1
    return -1
        
    
    # write your code here
    

if __name__ == '__main__':
    a = list(map(int,input().split()))
    n = a[0]
    a = a[1:]
    b = list(map(int,input().split()))
    k = b[0]
    b = b[1:]
    for i in b:
        if i > a[n-1] or i < a[0]:
            print("-1")
        else:
            print(binary_search(a,i,0,n-1),end = " ")
    print()
