# Uses python3
def get_change(m):
    #write your code here
    cnt = 0
    if m >= 10:
    	cnt += (m//10)
    	m-= (cnt*10)
    	if m == 0:
    		return cnt
    if m >= 5 and m < 10:
    	 k = (m//5)
    	 m -= (k*5)
    	 cnt+=k
    	 if m==0:
    	 	return cnt
    if m>=1 and m < 5:
    	cnt += m
    	return cnt 
    return cnt

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
