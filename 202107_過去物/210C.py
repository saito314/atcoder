import numpy as np

a, b = map(int, input().split())
canList = input().split()
np.zeros((a - b, b))

maxame = 0

for i in range(a - b + 1):
    tmp = set(canList[i : b + i])
    if maxame < len(tmp):
        maxame = len(tmp)
    if maxame == b:
        print(maxame)
        exit()

print(maxame)
