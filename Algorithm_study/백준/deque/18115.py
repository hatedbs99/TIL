import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
skill = list(map(int, input().split()))
dq = deque()

skill.reverse()

cur_card = 1
for i in skill:
    if i == 1:
        dq.appendleft(cur_card)
    elif i == 2:
        dq.insert(1, cur_card)
    elif i == 3:
        dq.append(cur_card)
    cur_card += 1

print(*dq)