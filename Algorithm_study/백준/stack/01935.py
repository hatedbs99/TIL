import sys
input = sys.stdin.readline

n = int(input())
s = input()
dic = {}
ord_num = 65
for _ in range(n):
    dic[chr(ord_num)] = int(input())
    ord_num += 1

stack = []

for i in s:
    if i == "*":
        stack.append(stack.pop() * stack.pop())
        continue
    elif i == "+":
        stack.append(stack.pop() + stack.pop())
        continue
    elif i == "-":
        stack.append(-stack.pop() + stack.pop())
        continue
    elif i == "/":
        temp = stack.pop()
        stack.append(stack.pop() / temp)
        continue
    elif i.isalpha():
        stack.append(dic[i])

print(f"{stack[0]:.2f}")
