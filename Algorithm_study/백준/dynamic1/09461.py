t = int(input())
array = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    array.append(array[i-5] + array[i-1])

for _ in range(t):
    n = int(input())
    print(array[n])


