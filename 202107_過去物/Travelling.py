a = int(input())

b = 0
c = 0
d = 0

for i in range(a):
    e, f, g = map(int, input())
    second = e - b
    if f < 0 and c < 0:
        f = -f
    x = f - c
    if g < 0:
        g = -g
    y = g - d
    distance = x + y

    if second < distance:
        print("NO")
    if second % 2 != distance % 2:
        print("NO")
