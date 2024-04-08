import numpy as np

maisuu, ave = map(int, input().split())
x = list(map(int, input().split()))

dp = np.zeros((maisuu + 1, maisuu + 1, 2501))
dp[0][0][0] = 1

for i in range(0, maisuu):
    for j in range(0, maisuu):
        for k in range(0, sum(x)):
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j + 1][k + x[i]] += dp[i][j][k]

ans = 0
for i in range(1, maisuu + 1):
    ans += dp[maisuu][i][i * ave]
print(int(ans))