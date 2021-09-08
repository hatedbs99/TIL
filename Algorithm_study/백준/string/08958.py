from sys import stdin
N = int(input())
for _ in range(N):
    n = stdin.readline().rstrip().split('X')
    result = 0
    for i in n:
        result += len(i) * (1 + len(i)) // 2
    print(result)

