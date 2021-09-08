from collections import deque
n, k = map(int, input().split())

array = deque()
result = []
for i in range(1, n+1):
    array.append(i)
while len(result) != n:
    for _ in range(k-1):
        array.append(array.popleft())
    result.append(array.popleft())

print("<", end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(f"{result[-1]}>")
