# 사례에 맞는 알고리즘을 알고 있어야 함
# 다익스트라 최단 경로 알고리즘
# 플로이드 워셜
# 벨만 포드 알고리즘
# 사실 그리디 알고리즘 및 다이나믹 알고리즘의 한 유형으로 볼 수 있다.

# 다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여
# 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
# '음의 간선'이 없을 때 정상적으로 동작
# 음의 간선이란 0보다 작은 값을 가지는 간선을 의미
# 실제로 GPS 소프트웨어의 기본 알고리즘으로 채택
# 매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복

import sys

input = sys.stdin.readline  # input()보다 빠르게 동작함
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    # 노드 a에서 노드 b로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 ,가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
