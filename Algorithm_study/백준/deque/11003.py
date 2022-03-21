import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
array = list(map(int, input().split()))
dq = deque()

for i in range(n):
    while dq and dq[-1][0] > array[i]:
        dq.pop()
    while dq and dq[0][1] < i-l+1:
        dq.popleft()
    dq.append((array[i], i))
    print(dq[0][0], end=' ')