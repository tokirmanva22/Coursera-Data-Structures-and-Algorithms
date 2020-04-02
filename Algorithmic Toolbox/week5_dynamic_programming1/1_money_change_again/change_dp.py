def coinschange(coin,n):
    a = [2000]*(n+1)
    a[0] = 0
    for j in coin:
        for i in range(j,n+1):
            a[i] = min(a[i],1 + a[i - j])
    return a[n]


if __name__ == '__main__':
    n = int(input())
    coin = [1,3,4]
    num = coinschange(coin,n)
    print(num)
        
        
    