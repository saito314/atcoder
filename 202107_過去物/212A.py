a = int(input())
b = int(input())

if 0 < a and b == 0:
    print("Gold")
elif a == 0 and b > 0:
    print("Silver")
elif a > 0 and b > 0:
    print("Alloy")
    