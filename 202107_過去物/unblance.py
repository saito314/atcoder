inStr = input()
s = set()

b = []
c = set(inStr)
for i in c:
    b.append(inStr.count(i))
maxNum = max(b)

for i in range(2, 4):
    if maxNum < (i / 2):
        break
    for j in range(0, len(inStr) + 1 - i):
        a = inStr[j : j + i]
        s = set(a)
        for k in s:
            cnt = a.count(k)
            if cnt > (len(a) / 2):
                print("{} {}".format(j + 1, j + i))
                exit()

print("-1 -1")