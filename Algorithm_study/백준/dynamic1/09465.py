t = int(input())
for _ in range(t):
    array = []
    n = int(input())

    for i in range(2):
        array.append(list(map(int, input().split())))

    if n != 1:
        array[0][1] += array[1][0]
        array[1][1] += array[0][0]

        for i in range(2, n):
            array[0][i] += max(array[1][i-1], array[1][i-2])
            array[1][i] += max(array[0][i-1], array[0][i-2])
        print(max(array[0][n-1], array[1][n-1]))
    else:
        print(max(array[0][0], array[1][0]))