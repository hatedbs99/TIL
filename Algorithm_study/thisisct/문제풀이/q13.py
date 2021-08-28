# 치킨배달
from itertools import combinations

INF = int(1e9)

n, m = map(int, input().split())
city = [[0] * (n + 1) for _ in range(n+1)]

chicken = []
house = []

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    city[i][1:] = data
    for j in range(1, n + 1):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

candidates = list(combinations(chicken, m))


def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = INF
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = INF
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
