n = int(input())

# set()은 집합 자료형을 초기화할 때 사용
# 특정 데이터가 존재하는지 검사할 때 매우 효과적으로 사용할 수 있다.
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')