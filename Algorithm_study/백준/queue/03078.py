from sys import stdin
N, K = map(int, stdin.readline().split())
students = [0] * N
name_len = [0] * 23
count = 0

for target in range(N):
    stu = len(stdin.readline())
    students[target] = stu

    if target > K:
        name_len[students[target-K-1]] -= 1

    count += name_len[stu]
    name_len[stu] += 1

print(count)