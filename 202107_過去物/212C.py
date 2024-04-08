a, b = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

minNum = 1000000000

for i in x:
    for j in y:
        res = abs(i - j)
        if res < minNum:
            minNum = res

print(minNum)