import sys
while True:
    s = sys.stdin.readline()
    dic = {')':'(', ']':'['}
    if s[0] == '.':
        break
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0 or stack.pop() != dic[i]:
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')