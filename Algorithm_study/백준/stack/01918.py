import sys

input = sys.stdin.readline

lst = list(input().strip())
stack = []
answer = ''

for i in lst:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
while stack:
    answer += stack.pop()
print(answer)

