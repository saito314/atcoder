a = []
for i in range(4):
    a.append(input())

h = "H"
b2 = "2B"
b3 = "3B"
hr = "HR"

if h in a:
    a.pop(a.index(h))
else:
    print("No")
    exit()
if b2 in a:
    a.pop(a.index(b2))
else:
    print("No")
    exit()
if b3 in a:
    a.pop(a.index(b3))
else:
    print("No")
    exit()
if hr in a:
    a.pop(a.index(hr))
else:
    print("No")
    exit()

print("Yes")