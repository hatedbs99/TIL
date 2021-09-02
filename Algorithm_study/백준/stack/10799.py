n = input()

index = 0
result = 0
for i in range(len(n)):
    if n[i] == '(':
        if n[i+1] == '(':
            index += 1
            result += 1
        else:
            result += index
    if n[i] == ')':
        if n[i-1] == '(':
            pass
        else:
            index -= 1

print(result)