import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    vps = sys.stdin.readline().rstrip()
    index = 0
    is_vps = True
    for i in vps:
        if i == '(':
            index += 1
        else:
            index -= 1
        # print(i, index)
        if index < 0:
            is_vps = False
            break
    if is_vps and index == 0:
        print("YES")
    else:
        print("NO")

