from sys import stdin
d = [0] * 41


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = fibonacci(n-1) + fibonacci(n-2)
        return d[n]


T = int(input())
for i in range(T):
    n = int(stdin.readline())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibonacci(n-1), fibonacci(n))
