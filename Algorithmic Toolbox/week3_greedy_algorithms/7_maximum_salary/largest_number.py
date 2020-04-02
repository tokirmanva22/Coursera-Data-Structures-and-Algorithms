# #Uses python3
# n = int(input())
# a = list(map(str,input().split()))
# a.sort(reverse=True)
# s = ''
# for i in a:
# 	if int(i+s) > int(s+i):
# 		s = i+s
# 	else:
# 		s += i
# print(s)
n = int(input())
lst = [int(i) for i in input().split()]


def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largestnumber(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer

print(''.join([str(i) for i in largestnumber(lst)]))
