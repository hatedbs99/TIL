n = int(input())
array = []
for _ in range(n):
    array.append(input())
dict = {}
for word in array:
    square_root = len(word) - 1
    for i in word:
        if i in dict:
            dict[i] += pow(10, square_root)
        else:
            dict[i] = pow(10, square_root)
        square_root -= 1

dict = sorted(dict.values(), reverse=True)
result, m = 0, 9
for value in dict:
    result += value * m
    m -= 1

print(result)


