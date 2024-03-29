def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
target_array = list(map(int, input().split()))

for i in target_array:
    result = binary_search(array, i, 0, n - 1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
