import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
result = 0

for _ in range(m):
    price = tuple(map(int, input().split()))
    lst.append(price)

package = sorted(lst, key=lambda x: x[0])
each = sorted(lst, key=lambda x: x[1])

if package[0][0] <= each[0][1] * 6:
    result = package[0][0] * (n // 6) + each[0][1] * (n % 6)
    if package[0][0] < each[0][1] * (n % 6):
        result = package[0][0] * (n // 6 + 1)

else:
    result = each[0][1] * n

print(result)
