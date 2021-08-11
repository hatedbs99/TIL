# 삽입 정렬은 데이터가 정렬되어 있을 때 효율적
# 특정한 데이터를 적절한 위치에 삽입

# 삽입정렬 메서드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break


print(array)
