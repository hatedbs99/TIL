import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1], x[0]))
for i in lst:
    print(i[0], i[1])