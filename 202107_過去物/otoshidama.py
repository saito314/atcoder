a, b = map(int, input().split())

for i in range(a + 1):
    for j in range(a + 1 - i):
        if 10000 * i + 5000 * j + 1000 * (a - i - j) == b:
            print("{} {} {}".format(i, j, a - i - j))
            exit()

print("-1 -1 -1")