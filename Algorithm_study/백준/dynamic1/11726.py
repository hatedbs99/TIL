d = [0] * 1001


def pibo(n):
    if n <= 2:
        return n
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = pibo(n-2) + pibo(n-1)
        return d[n]


print(pibo(int(input())) % 10007)
