t = int(input())
array = [300, 60, 10]
result = []
for i in array:
    result.append(t // i)
    t = t % i

if t != 0:
    print(-1)
else:
    for i in range(3):
        print(result[i], end=' ')

