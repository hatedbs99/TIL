import sys
k = int(input())
array = []
for _ in range(k):
    m = int(sys.stdin.readline())
    if m == 0 and array:
        array.pop()
    else:
        array.append(m)
print(sum(array))