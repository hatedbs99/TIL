import sys
n = int(input())
s = []
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    string = command[0]
    if string == 'push':
        s.append(command[1])
    elif string == 'pop':
        print(s.pop() if s else -1)
    elif string == 'size':
        print(len(s))
    elif string == 'empty':
        print(1 if not s else 0)
    elif string == 'top':
        print(s[-1] if s else -1)
