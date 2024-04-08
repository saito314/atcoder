a = input()

length = len(a) - 1
sum = 0
for i in range(2 ** length):
    tmp = []
    for j in range(length):
        if (i >> j) & 1:
            tmp.append("+")
        else:
            tmp.append("")
    
    formula = ""
    for b, c in zip(a, tmp + [""]):
        print(c)
        formula += (b + c)
    sum += eval(formula)

print(sum)