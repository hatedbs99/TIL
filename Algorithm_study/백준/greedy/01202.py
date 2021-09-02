import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
jewelry = []
for _ in range(n):
    heapq.heappush(jewelry, list(map(int, sys.stdin.readline().split())))
bags = [int(sys.stdin.readline()) for _ in range(k)]
bags.sort()
temp = []
result = 0
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewelry)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not jewelry:
        break
print(result)