import sys

input = sys.stdin.readline

arr = []

for _ in range(int(input())):
    arr.append(int(input()))

stack = [arr[1]]
temp = 0
for i in range(1, len(arr)+1):
    if arr[i] >= arr[i-1]:
        temp += arr[i-1]

    else:
        if stack[-1]