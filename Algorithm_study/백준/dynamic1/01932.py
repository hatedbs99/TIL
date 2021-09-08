import sys
n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    for j in range(len(array[i])):
        if j == 0:
            array[i][j] = array[i][j] + array[i-1][j]
        elif j == len(array[i]) - 1:
            array[i][j] = array[i][j] + array[i-1][j-1]
        else:
            array[i][j] = max(array[i-1][j-1], array[i-1][j]) + array[i][j]
print(max(array[n-1]))