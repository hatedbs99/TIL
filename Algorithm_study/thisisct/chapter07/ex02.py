# 우선순위 큐를 구현할 떄 Heap을 이용
# 최소 힙을 이용하는 경우 값이 낮은 데이터가 먼저 삭제
# 최대 힙을 이용하는 경우 값이 큰 데이터가 먼저 삭제
# 최소 힙을 최대 힙처럼 사용하기 위해서 일부러 우선순위에 해당하는 값에 음스부호를 붙여서 넣었다가,
# 나중에 우선순위 큐에서 꺼낸 다음에 다시 음수 부호를 붙여서 원래의 값으로 돌리는 방식을 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
