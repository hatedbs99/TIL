n, k = map(int, input().split())
coin_list = []
dp = [0 for _ in range(k+1)]
dp[0] = 1
for _ in range(n):
    coin_list.append(int(input()))
for i in coin_list:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])
