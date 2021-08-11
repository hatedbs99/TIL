# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 최악의 경우에도 수행시간 O(N + K)
# 별도의 리스트를 선언하고ㅗㅗ 그 안에 정렬에 대한 정보를 담는다.


# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

result = []


for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        # print(i, end=' ')
        result.append(i)

print(result)
