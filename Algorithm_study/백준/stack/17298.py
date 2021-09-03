import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = [0] # 스택을 index로 활용

for i in range(1, n):
    while stack and array[stack[-1]] < array[i]:
        answer[stack.pop()] = array[i]
    stack.append(i)
print(*answer)
