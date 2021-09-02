# from collections import deque
# a, b = map(int, input().split())
#
# res = -1
# que = deque([(a, 1)])
# while que:
#
#     i, count = que.popleft()
#     if i == b:
#         res = count
#         break
#     if i*2 <= b:
#         que.append((i*2, count + 1))
#     if int(str(i) + '1') <= b:
#         que.append((int(str(i) + '1'), count + 1))
#
# print(res)

a, b = map(int, input().split())
count = 1
while True:
    print(b)
    if b == a:
        print(count)
        break
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        count = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            count += 1
        else:
            b //= 2
            count += 1

