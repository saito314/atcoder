inStr = input()
s = set()

b = []
c = set(inStr)
for i in c:
    b.append(inStr.count(i))
maxNum = max(b)

for i in range(2, len(inStr) + 1):
    if maxNum < (i / 2):
        break
    for j in range(0, len(inStr) + 1 - i):
        a = inStr[j : j + i]
        s = set(a)
        lis = [[j+1, j+i] for k in s if a.count(k) > (len(a) /2)]
        if len(lis) > 0:
            print("{} {}".format(lis[0][0], lis[0][1]))
            exit()

print("-1 -1")