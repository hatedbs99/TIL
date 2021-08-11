# 정렬이란? 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
# 데이터를 정렬하면 이진 탐색(Binary Search)이 가능

# 선택 정렬
# 매번 가장 작은 것을 선택

# 선택정렬 메서드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
