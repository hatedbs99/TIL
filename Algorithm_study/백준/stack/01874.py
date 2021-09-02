import sys
n = int(sys.stdin.readline())
array = []
result = []
count = 1
possible = True
for _ in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        array.append(count)
        result.append('+')
        count += 1
    if array[-1] == num:
        array.pop()
        result.append('-')
    else:
        possible = False

if not possible:
    print('NO')
else:
    for i in result:
        print(i)