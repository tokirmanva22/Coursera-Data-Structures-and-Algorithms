d = int(input())
rf = int(input())
n = int(input())
a = list(map(int,input().split()))
a.append(d)
if rf >= d:
    print(0)
else:
    n += 1
    i = 0
    init = 0
    flg = 0
    cnt = 0
    while i < n :
        d = a[i] - init
        if d > rf:
            i = i-1
            cnt += 1
            if init == a[i]:
                flg = 1
                print(-1)
                break
            init = a[i]
        i+=1
    if flg == 0:
        print(cnt)