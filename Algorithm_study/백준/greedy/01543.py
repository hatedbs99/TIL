doc = str(input())
target = str(input())
result = 0
temp = 0

while True:
    if doc[temp:(temp+len(target))] == target:
        result += 1
        temp += len(target)
    else:
        temp += 1

    if temp + len(target) > len(doc):
        break

print(result)
