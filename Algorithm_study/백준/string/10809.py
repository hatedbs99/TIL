array = list(map(chr, range(97, 123)))

s = input()

for i in array:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')
