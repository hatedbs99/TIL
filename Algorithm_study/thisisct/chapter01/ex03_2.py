# n, m, k를 쉼표로 구분하여 입력받음
n, m, k = map(int, input().split(","))
# N개의 수를 쉼표로 구분하여 입력받기
data = list(map(int, input().split(",")))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0
count = int(m / (k+1)) * k
count += m % (k + 1)

result += (count) * first
result += (m - count) * second

print(result)