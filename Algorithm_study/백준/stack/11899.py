arr = input().rstrip()
stack = []
answer = 0
for i in arr:
    if i == '(':
        stack.append(i)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            answer += 1

print(answer + len(stack))
