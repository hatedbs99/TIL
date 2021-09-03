import sys
s = sys.stdin.readline().strip()
stack = []
answer = 0
for i in s:
    if i in ['(', '[']:
        stack.append(i)

    elif i == ')':
        temp = 0
        if len(stack) == 0:
            print(0)
            sys.exit(0)
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                print(0)
                sys.exit(0)
            elif top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(temp * 2)
                break
            else:
                temp += top
    elif i == ']':
        temp = 0
        if len(stack) == 0:
            print(0)
            sys.exit(0)
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                print(0)
                sys.exit(0)
            elif top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(temp * 3)
                break
            else:
                temp += top

    else:
        print(0)
        sys.exit(0)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        sys.exit(0)
    else:
        answer += i
print(answer)