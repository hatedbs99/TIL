string = input()
string = string.upper()

dic = {}
for s in string:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

answer = 0
is_same = False
for s in dic:
    if dic[s] > answer:
        answer = dic[s]
        is_same = False
    elif dic[s] == answer:
        is_same = True

print(answer if not is_same else '?')
