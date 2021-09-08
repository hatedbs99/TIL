from sys import stdin
from collections import deque
N = int(stdin.readline())
queue = deque()
while True:
    n = int(stdin.readline())
    if n == -1:
        break
    if n == 0:
        queue.popleft()
    elif n != 0 and len(queue) < N:
        queue.append(n)
if queue:
    print(*queue)
else:
    print("empty")
