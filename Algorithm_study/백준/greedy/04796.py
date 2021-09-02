import sys

i = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l + p + v == 0:
        break
    result = ((v // p) * l) + min((v % p), l)
    print("Case {}: {}".format(i, result))
    i += 1
