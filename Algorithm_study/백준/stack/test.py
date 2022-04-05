import sys
lst = []
while True:
    input = sys.stdin.readline().rstrip()
    if '-' in input:
        break
    lst.append(input)
res = []
for data in lst:
    stack = []
    cnt = 0
    for i in data:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-2] == '{' and stack[-1] == '}':
                stack.pop()
                stack.pop()
    res.append(stack)
for st in res:
    cnt = 0
    for i in range(0, len(st), 2):
        if st[i] + st[i + 1] == "{" + "{":
            cnt += 1
        elif st[i] + st[i + 1] == "}" + "}":
            cnt += 1
        elif st[i] + st[i + 1] == "}{":
            cnt += 2
    print(res.index(st) + 1, ". ", cnt, sep = '')