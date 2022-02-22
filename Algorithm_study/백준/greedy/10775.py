g = int(input())
p = int(input())
lst = [int(input()) for _ in range(p)]
result = [-1 for _ in range(g+1)]

answer = 0
for i in lst:
    while i > 0:
        if result[i] == -1:
            result[i] = 0
            answer += 1
            break
        i -= 1
    if i == 0:
        break
print(answer)