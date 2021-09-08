s = input()
for i in range(len(s) // 10):
    if len(s) >= 10:
        print(s[:10])
        s = s[10:]
if s:
    print(s)