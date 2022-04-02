n = int(input())
arr = []
cnt = 1

for _ in range(n):
    arr.append(input().rstrip())


for i in arr:
    stack = i.split()
    print(f'Case #{cnt}: ', end='')
    while stack:
        print(stack.pop(), end=' ')
    print()
    cnt += 1
