n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
temp = 0
for i in p:
    temp += i
    result += temp
print(result)