import sys

input = sys.stdin.readline
answer = 1
arr = []
for _ in range(int(input())):
    arr.append(int(input()))

tmp = arr.pop()
# for i in range(len(arr)-1, -1, -1):
#

while arr:
    if arr[-1] > tmp:
        answer += 1
        tmp = arr.pop()
    else:
        arr.pop()

print(answer)