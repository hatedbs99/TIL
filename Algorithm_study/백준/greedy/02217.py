n = int(input())
rope = []
result = []
for _ in range(n):
    r = int(input())
    rope.append(r)
rope.sort(reverse=True)
for i in range(n):
    result.append(rope[i] * (i+1))
print(max(result))