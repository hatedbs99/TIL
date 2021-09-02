n = int(input())
array = list(map(int, input().split()))
array.sort()
result = 1
for i in range(n):
    if result < array[i]:
        break
    result += array[i]
print(result)

