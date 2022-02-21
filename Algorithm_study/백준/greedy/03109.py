import sys
input = sys.stdin.readline
r, c = map(int ,input().split())
area = [list(map(str, input().strip())) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
dx = [-1, 0, 1]
dy = [1, 1, 1]
result = 0

def go(a, b):
    if b == c-1:
        return True
    for j in range(3):
        nx = a + dx[j]
        ny = b + dy[j]
        if (0 <= nx < r) and (0 <= ny < c) and not visit[nx][ny] and area[nx][ny] == '.':
            visit[nx][ny] = True
            if go(nx, ny):
                return True
    return False

for i in range(r):
    if area[i][0] == '.':
        if go(i, 0):
            result += 1

print(result)
