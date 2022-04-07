import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
ab = []
for _ in range(n):
    lst.append(int(input()))


for _ in range(m):
    a, b = map(int, input().split())
    print(min(lst[a-1:b]), max(lst[a-1:b]))