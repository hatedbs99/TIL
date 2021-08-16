# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)
#
# print(fibo(100)) # 계산이 엄청 오래걸림


# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100


def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# 이처럼 재귀 함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법을 탑다운방식이라고 함
# 큰 문제를 해결하기 위해 작은 문제를 호출

# 단순히 반복문을 이용하여 소스코드를 작성하는 경우 보텀업 방식이라고 함
# 작은 문제부터 차근차근 답을 도출

# 시간복잡도 O(N)
# 다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어
# 문제를 효율적으로 해결하는 알고리즘 기법

