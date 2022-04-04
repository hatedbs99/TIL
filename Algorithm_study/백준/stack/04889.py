array = []
num = 1
while True:
    array.append(input().rstrip())
    if array[-1][0] == "-":
        array.pop()
        break

for i in array:
    stack = []
    answer = 0

    for j in i:
        if j == '{':
            stack.append(j)
        elif j == '}' and not stack:
            answer += 1
            stack.append('{')
        elif j == '}' and stack[-1] == '{':
            stack.pop()
    answer += len(stack) // 2
    print(f'{num}. {answer}')
    num += 1
