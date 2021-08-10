# n, m, k를 쉼표로 구분하여 입력받음
n, m, k = map(int, input().split(","))
# N개의 수를 쉼표로 구분하여 입력받기
data = list(map(int, input().split(",")))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0: # m이 0일때 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기

    if m == 0:
        break # m이 0일 때 탈출

    result += second # 두 번째로 큰 수 더하기
    m -= 1

print(result)