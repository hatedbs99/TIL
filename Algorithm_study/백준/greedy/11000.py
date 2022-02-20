import sys
import heapq
input = sys.stdin.readline
heap = []

n = int(input())
class_lst = []

for _ in range(n):
    s, t = map(int, input().split())
    class_lst.append([s, t])
class_lst.sort(key=lambda x: x[0]) # 각 배열의 0번째를 기준으로 정렬
heapq.heappush(heap, class_lst[0][1])
for i in range(1, n):
    if heap[0] > class_lst[i][0]:
        heapq.heappush(heap, class_lst[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, class_lst[i][1])

print(len(heap))