a = input()
length = len(a)

dp = [[0 for i in range(9)] for j in range(length)]
dp[0] = 1
chokudai = "chokudai"

for i in range(langth):
    for j in range(8):
        