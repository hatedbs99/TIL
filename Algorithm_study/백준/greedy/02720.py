import sys
input = sys.stdin.readline

t = int(input())
coin_type = [25, 10, 5, 1]
test_case = [int(input()) for _ in range(t)]
for i in test_case:
    temp = i
    for j in coin_type:
        print(temp // j, end=" ")
        temp = temp % j
    print()
