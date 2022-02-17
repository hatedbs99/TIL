import sys

data = [sys.stdin.readline() for _ in range(int(input()))]

print(data)
data.sort(key=lambda x: tuple(map(int, x.split())))
# data.sort(key=lambda x: (x[0], x[1]))
print(data)
print("".join(data))

