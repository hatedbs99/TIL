n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

# a.sort()
# b.sort()
#
# a = a[k:]
# b = b[-k:]
#
# for i in range(k):
#     a.append(b[i])
#
# print(sum(a))
