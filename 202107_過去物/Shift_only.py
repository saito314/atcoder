a = input()

evenCount = 0
b = input().split()
c = []

while True:
    for i in b:
        if int(i) % 2 == 0:
            c.append(int(i) / 2)
            continue
        else:
            break
    else:
        b = []
        b = c
        c = []
        evenCount = evenCount + 1
        continue
    break

print(evenCount)