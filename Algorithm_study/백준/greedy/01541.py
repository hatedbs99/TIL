a = input()
is_plus = True
index = 0
index_now = 0
plus_list = []
minus_list = []
for i in range(len(a)):
    if a[i] == '+':
        if is_plus:
            plus_list.append(int(a[index:i]))
            index = i + 1
        else:
            minus_list.append(int(a[index:i]))
            index = i + 1

    elif a[i] == '-':
        if is_plus:
            plus_list.append(int(a[index:i]))
            index = i + 1
            is_plus = False
        else:
            minus_list.append(int(a[index:i]))
            index = i + 1
            is_plus = False

    if i == len(a) - 1:
        if is_plus:
            plus_list.append(int(a[index:i+1]))
        else:
            minus_list.append(int(a[index:i+1]))

result = sum(plus_list) - sum(minus_list)
print(result)