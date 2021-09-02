n = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
min_price = oil_price[0]
total = road[0] * oil_price[0]
for i in range(1, n-1):
    min_price = min(min_price, oil_price[i])
    total += min_price * road[i]
print(total)

