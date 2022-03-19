
apple_lst = []
turn_lst = []
n = int(input())
k = int(input())

for _ in range(k):
    apple_lst.append(list(map(int, input().split())))

l = int(input())
for _ in range(l):
    c, d = input().split()
    turn_lst.append([int(c), d])
