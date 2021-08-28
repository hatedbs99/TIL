from itertools import permutations


def is_prime_number(x):
    x = int(x)
    if x == 1 or x == 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numbers.sort()
    temp_list = []
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        for j in temp:
            j = int("".join(j))
            if j in temp_list:
                continue
            temp_list.append(j)
            if is_prime_number(j):
                answer += 1
    return answer


print(solution("011"))