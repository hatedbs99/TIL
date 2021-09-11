from sys import stdin
import math

t = int(input())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(result)