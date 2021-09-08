from sys import stdin

n = int(input())
array = [0]

for _ in range(n):
    array.append(int(stdin.readline()))

dp = [0, array[1]]
if n >= 2:
    dp.append(sum(array[1:3]))
if n >= 3:
    for i in range(3, n+1):
        dp.append(max(dp[i-1], dp[i-3] + array[i-1] + array[i], dp[i-2] + array[i]))
print(dp[n])