a = input()
s = {0 : [], 1 : [], 2 : [], 3 :[] , 4 : [], 5 : [], 6 : [], 7 :[]}
schr = ["i", "a", "d", "u", "k", "o", "h", "c"]

b = list(reversed(a))
a = ''.join(b)

while True:
    if a == "":
        break
    for i in range(8):
        tmp = a.find(schr[i])
        print(i)
        if tmp == -1:
            print(schr[i])
            if schr[i] == "c":
                print(int(sum(s[7]) % (10 ** 9 + 7)))
                exit()
            continue
        a = a[tmp:]
        if i == 0:
            s[i].append(1)
        elif not s[i]:
            s[i].append(1)
        else:
            s[i].append(sum(s[i - 1]))

print(int(sum(s[7]) % (10 ** 9 + 7)))