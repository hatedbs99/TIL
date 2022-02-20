import sys
input = sys.stdin.readline
score = []
answer = 0

n = int(input())
for _ in range(n):
    score.append(int(input()))

for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        answer += score[i] - score[i+1] + 1
        score[i] = score[i+1] - 1

print(answer)

