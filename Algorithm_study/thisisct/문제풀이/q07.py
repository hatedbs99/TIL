n = input()
n_list = list(map(int, str(n)))

print(len(n_list))

test = n_list[:3]
print(test)

lucky = sum(n_list[:(len(n_list) // 2)])
strike = sum(n_list[(len(n_list) // 2):])

if lucky == strike:
    print("LUCKY")
else:
    print("READY")

