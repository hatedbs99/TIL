n, m = map(int, input().split())
data = list(map(int, input().split()))
#
# data.sort()
# count = 0
# print(data)
# for i in range(n):
#     for j in range(n):
#         if data[i] != data[j]:
#             count += 1
#
# print(count // 2)

array = [0] * 11
for x in data:
    array[x] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
