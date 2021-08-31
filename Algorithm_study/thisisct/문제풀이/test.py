a, b = map(int, input().split())
n = max(a, b)
while True:
    n -= 1
    if a % n == 0 and b % n ==0:
        print(n)
        break