n, k = map(int, input().split())
coin_list = []
count = 0
now = 0
for _ in range(n):
    a = int(input())
    coin_list.append(a)

coin_list.sort(reverse=True)
for coin in coin_list:
    if coin <= k:
        count += k // coin
        k = k % coin

print(count)