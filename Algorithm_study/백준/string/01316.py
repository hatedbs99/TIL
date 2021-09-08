from sys import stdin
n = int(input())
count = 0

for _ in range(n):
    s = stdin.readline()
    array = []
    now = '0'
    tof = True
    for i in s:
        if i == now:
            continue

        if i not in array:
            array.append(i)
            now = i
        else:
            tof = False

    if tof:
        count += 1


print(count)
