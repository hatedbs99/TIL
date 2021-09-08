from sys import stdin

n = int(stdin.readline())
d = [0] * 300
step = [0] * 300

for i in range(n):
    step[i] = int(stdin.readline())

d[0] = step[0]
d[1] = step[0] + step[1]
d[2] = max(step[0] + step[2], step[1] + step[2])
for i in range(3, n):
    d[i] = max(d[i-3] + step[i-1] + step[i], d[i-2] + step[i])

print(d[n-1])
