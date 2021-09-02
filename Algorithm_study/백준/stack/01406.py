import sys
stack = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
temp = []
for _ in range(m):
    command = list(sys.stdin.readline().split())

    if command[0] == "L" and len(stack) != 0:
        temp.append(stack.pop())
    elif command[0] == "D" and len(temp) != 0:
        stack.append(temp.pop())
    elif command[0] == "B" and len(stack) != 0:
        stack.pop()
    elif command[0] == "P":
        stack.append(command[1])

for _ in range(len(temp)):
    stack.append(temp.pop())

print("".join(stack))