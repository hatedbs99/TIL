n = int(input())
array = list(map(int, input().split()))
s = [array[0]]
for i in range(len(array)-1):
    s.append(max(s[i] + array[i+1], array[i+1]))
print(max(s))

