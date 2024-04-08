inStr = input()
inSet = set(inStr)

for i in inSet:
    num = inStr.count(i)
    if num % 2 == 0:
        continue
    else:
        print("No")
        exit()

print("Yes")
