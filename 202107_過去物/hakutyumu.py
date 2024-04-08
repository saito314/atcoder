useStr = ["dream", "dreamer", "erase", "eraser"]
inputStr = input()

while True:
    for i in useStr:
        if inputStr == i:
            print("YES")
            exit()
        if inputStr.endswith(i):
            a = len(i)
            inputStr = inputStr[:-a]
            break
    else:
        print("NO")
        exit()
