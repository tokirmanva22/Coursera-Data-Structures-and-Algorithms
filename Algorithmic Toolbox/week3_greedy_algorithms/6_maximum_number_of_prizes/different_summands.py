n = int(input())

total = 0
increment = 1
count = 0
listOfNum = []

while total + increment <= n:
    total += increment
    listOfNum.append(increment)
    increment += 1
    count += 1

listOfNum[count-1] += n - total

print(count)
print(*listOfNum)