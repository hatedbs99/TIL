from sys import stdin

n = int(input())
tree = [[] for i in range(n + 1)]

for _ in range(n):
    l = list(map(int, stdin.readline().split()))
    for i in range(1, len(l)-2, 2):
        tree[l[0]].append((l[i], l[i+1]))

print(tree)

#
# q = [1]
# ans = {}
# check = [False for i in range(n+1)]
#
# while len(q) > 0:
#     parent = q.pop(0)
#     for i in tree[parent]:
#         if not check[i]:
#             ans[i] = parent
#             q.append(i)
#             check[i] = True
#
# for i in range(2, n+1):
#     print(ans[i])
