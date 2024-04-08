dp = [[[] * 210] * 210] * 20

for i in range(20):
    dp[i + 1][i].append("a")