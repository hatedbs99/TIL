from collections import deque
import sys
tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))
    count = 0
    while queue:
        top = max(queue)
        m -= 1
        pop = queue.popleft()
        if top != pop:
            queue.append(pop)
            if m < 0:
                m = len(queue) - 1
        else:
            count += 1
            if m == -1:
                print(count)
                break
