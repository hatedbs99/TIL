import sys
from collections import deque

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    dq = deque()
    n = int(input())
    arr = list(map(str, input().split()))
    for i in arr:
        if not dq:
            dq.append(i)
            continue

        if ord(dq[0]) >= ord(i):
            dq.appendleft(i)
        else:
            dq.append(i)

    print("".join(dq))