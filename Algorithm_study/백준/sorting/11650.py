import sys
l = []

n = int(input())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))
l.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    print(l[i][0], l[i][1])