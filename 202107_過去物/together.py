num = int(input())
numList = list(map(int, input().split()))

minCost = 9223372036854775807
for i in range(minNum + 1, maxNum):
    a = 0
    for j in numList:
        try:
            a = a + (j - i)**2
        except OverflowError:
            break
    if a < minCost:
        minCost = a

print(minCost)