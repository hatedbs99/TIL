import sys
import heapq

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    heapq.heappush(array, int(sys.stdin.readline()))

if len(array) == 1:
    print(0)
else:
    answer = 0
    while len(array) > 1:
        temp_1 = heapq.heappop(array)
        temp_2 = heapq.heappop(array)
        answer += temp_1 + temp_2
        heapq.heappush(array, temp_1 + temp_2)
    print(answer)