import sys

input = sys.stdin.readline
t = int(input())
array = [[] for _ in range(t)]
for i in range(t):
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        array[i].append([a, b])


def solution(lst):
    count = 1
    lst.sort()
    maximum = lst[0][1]
    for i in range(1, len(lst)):
        if maximum > lst[i][1]:
            count += 1
            maximum = lst[i][1]
    print(count)


for i in range(t):
    solution(array[i])
