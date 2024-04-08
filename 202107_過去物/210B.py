n = int(input())
s = input()
cnt = 1

for i in s:
    if i == "1":
        if cnt % 2 == 1:
            print("Takahashi")
        else:
            print("Aoki")