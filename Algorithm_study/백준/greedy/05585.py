money = 1000
n = money - int(input())
coin_type = [500, 100, 50, 10, 5, 1]
result = 0
for coin in coin_type:
    result += n // coin
    n = n % coin

print(result)