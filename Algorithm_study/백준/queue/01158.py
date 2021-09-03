from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
queue = deque()
result = []
for i in range(1, n+1):
    queue.append(i)

while len(result) != n:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(f"{result[-1]}>")
