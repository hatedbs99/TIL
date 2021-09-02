import sys

s = sys.stdin.readline()
while True:
    dic = {')': '(', ']': '['}
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        # elif i == ')' or i == ']':
            # if len(stack) == 0 or stack.pop() != dic[i]:
            #     print(0)
            #     break
        elif i == ')':
            if stack[-1] == '('
                result += 2