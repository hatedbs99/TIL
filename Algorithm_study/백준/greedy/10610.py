n = int(input())

n_list = list(map(int, str(n)))
n_list.sort(reverse=True)

if (sum(n_list) % 3) != 0 or n_list[-1] != 0:
    print(-1)
else:
    n_list = map(str, n_list)
    print("".join(n_list))
