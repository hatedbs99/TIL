n, k = map(int, input().split())
s = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(k):
    if s[i] in plug:
        continue
    if len(plug) < n:
        plug.append(s[i])
        continue

    idxs = []
    for j in range(n):
        try:
            idx = s[i:].index(plug[j])
        except ValueError:
            idx = 101
        idxs.append(idx)
    plug_out = idxs.index(max(idxs))
    del plug[plug_out]
    plug.append(s[i])
    cnt += 1
print(cnt)
