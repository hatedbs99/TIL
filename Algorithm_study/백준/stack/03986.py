import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(input().rstrip())

ans = 0

for i in lst:
    stack = []
    for j in i:
        stack.append(j)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if not stack:
        ans += 1

#
# for i in lst:
#     stack = []
#     for j in i:
#
#         if stack and stack[-1] == j:
#             stack.pop()
#         else:
#             stack.append(j)
#     if not stack:
#         ans += 1

print(ans)
