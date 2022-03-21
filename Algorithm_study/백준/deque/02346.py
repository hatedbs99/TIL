import sys
from collections import deque

input = sys.stdin.readline
answer = []
n = int(input())
dq = deque(enumerate(map(int, input().split())))

while dq:
    idx, num = dq.popleft()
    answer.append(idx + 1)
    if num > 0:
        dq.rotate(-(num-1))
        print(-(num-1))
    else:
        dq.rotate(-num)
        print(-num)

print(" ".join(map(str, answer)))
