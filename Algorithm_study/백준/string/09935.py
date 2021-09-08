s = input()
bomb = input()

last = bomb[-1]
stack = []
length = len(bomb)

for char in s:
    stack.append(char)
    if char == last and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
