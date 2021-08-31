import sys
n = int(input())
time_list = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time_list.append((start, end))

time_list.sort(key=lambda x: (x[1], x[0]))
count = 0
end_time = 0

for start, end in time_list:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
