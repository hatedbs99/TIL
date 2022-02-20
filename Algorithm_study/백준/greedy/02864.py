# a, b = map(int, input().split())
#
# a_list = list(map(int, str(a)))
# b_list = list(map(int, str(b)))
# min_a = []
# max_a = []
# min_b = []
# max_b = []
# for i in a_list:
#     if i == 5 or i == 6:
#         min_a.append(5)
#         max_a.append(6)
#     else:
#         min_a.append(i)
#         max_a.append(i)
#
# for j in b_list:
#     if j == 5 or j == 6:
#         min_b.append(5)
#         max_b.append(6)
#     else:
#         min_b.append(j)
#         max_b.append(j)
#
# min_a = "".join(map(str, min_a))
# max_a = "".join(map(str, max_a))
# min_b = "".join(map(str, min_b))
# max_b = "".join(map(str, max_b))
#
# print(int(min_a) + int(min_b), end=" ")
# print(int(max_a) + int(max_b))

import sys

a, b = sys.stdin.readline().split()

# minimum
a = a.replace('6', '5')
b = b.replace('6', '5')

print(int(a) + int(b), end=' ')
# maximum
a = a.replace('5', '6')
b = b.replace('5', '6')

print(int(a) + int(b))
