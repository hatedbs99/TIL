import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))
nums.sort(reverse=True)
for num in nums:
    print(num)