from sys import stdin; input = stdin.readline
from collections import deque


n = int(input())
tree = [[] for i in range(n + 1)]

for _ in range(n):
    node = 0
    tmp_list = list(map(int, input().split()))
    for i in range(1, len(tmp_list)-1, 2):
        tree[tmp_list[0]].append((tmp_list[i], tmp_list[i+1]))

answer = 0


def bfs(start):
    global answer
    visit = [-1] * (n + 1)
    visit[start[0]] = 0
    q = deque([start])
    rt = (0, 0)
    while q:
        cur, w = q.popleft()
        for adj, adj_w in tree[cur]:
            if visit[adj] != -1:
                continue
            visit[adj] = visit[cur] + adj_w
            q.append((adj, adj_w))
            if rt[1] < visit[adj]:
                rt = (adj, visit[adj])
    return rt

rt = bfs((1, 0))
answer = bfs((rt[0], 0))
print(answer[1])
