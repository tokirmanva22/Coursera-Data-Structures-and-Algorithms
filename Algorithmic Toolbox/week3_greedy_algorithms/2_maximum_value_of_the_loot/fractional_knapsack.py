# Uses python3
def get_optimal_value(arr,cap,n):
    value = 0
    # write your code here
    i = 0
    while cap > 0 and i < n:
        c = min(cap,arr[i][2])
        value += (c*arr[i][0])
        i+=1
        cap -= c
    # print()
    return value


if __name__ == "__main__":
    n,cap = map(int,input().split())
    arr = []
    for i in range(n):
        a,b = map(int,input().split())
        arr.append([a/b,a,b])
    arr.sort(reverse = True)
    opt_value = get_optimal_value(arr,cap,n)
    # print(arr)
    print("{:.4f}".format(opt_value))
