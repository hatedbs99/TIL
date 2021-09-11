n = int(input())
dp = [[0] * 10] * (n+1)
dp[1] = [1] * 10
for i in range(2, n+1):
    for j in range(10, 0, -1):
        dp[i][j-1] = dp[i-1][j-1] * j
print(dp)
print(sum(dp[n]))

