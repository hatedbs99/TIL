import sys
n = int(input())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0 for _ in range(n)]
for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tower[i]])
print(*answer)













# n = int(input())
# tower = list(map(str, sys.stdin.readline().split()))
# laser = []
# temp = []
# while len(tower) != 0:
#     now = tower.pop()
#     for i in range(len(tower)):
#         k = len(tower)
#         if now > tower[-1]:
#             temp.append(tower.pop())
#         else:
#             laser.append(k)
#             for _ in range(len(temp)):
#                 tower.append(temp.pop())
#             break
#
#     else:
#         laser.append(0)
#         for _ in range(len(temp)):
#             tower.append(temp.pop())
# laser = list(map(str, laser))
# laser.reverse()
# print(' '.join(laser))

