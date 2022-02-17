import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = 1
start = lst[0]
for i in range(1, n):
    if lst[i]-start >= l:
        result += 1
        start = lst[i]

print(result)
