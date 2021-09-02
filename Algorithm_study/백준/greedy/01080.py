n, m = map(int, input().split())
array = [list(map(int, input().strip())) for _ in range(n)]
to_array = [list(map(int, input().strip())) for _ in range(n)]
result = 0


def turn(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            array[x][y] = 1 - array[x][y]


for i in range(n-2):
    for j in range(m-2):
        if array[i][j] != to_array[i][j]:
            turn(i, j)
            result += 1

if array == to_array:
    print(result)
else:
    print(-1)