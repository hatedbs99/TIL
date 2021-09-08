from sys import stdin
from collections import deque
T = int(input())
for _ in range(T):
    p = stdin.readline().strip()
    n = int(stdin.readline())
    temp = stdin.readline().strip()
    error = False
    reverse = False
    if len(temp) == 2:
        array = []
    else:
        array = deque(map(int, temp[1:-1].split(',')))
    for i in p:
        if i == 'R':
            if array and reverse:
                reverse = False
            elif array and not reverse:
                reverse = True
        if i == 'D':
            if array and reverse:
                array.pop()
            elif array and not reverse:
                array.popleft()
            else:
                error = True
                break
    if not error and array:
        if reverse:
            array.reverse()
        print('[', end='')
        for i in range(len(array)-1):
            print(f'{array[i]},', end='')
        print(array[len(array)-1], end='')
        print(']')
    elif not error and not array:
        print('[]')
    else:
        print('error')
