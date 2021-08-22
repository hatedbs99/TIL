# 그래프 구현 방법
# 인접 행렬: 2차원 배열을 사용하는 방식
# 인접 리스트: 리스트를 사용하는 방식

# 노드의 개수가 V, 간선의 개수가 E인 그래프

# 간선정보 저장
# 인접 행렬의 경우 O(V^2)만큼의 메모리 공간 필요
# 인접 리스트의 경우 O(E)만큼의 메모리 공간 필요

# 인접 행렬은 간선의 비용을 O(1)의 시간으로 즉시 알 수 있음
# 인텁 리스트의 경우 O(V)만큼의 시간 소요

# 다익스트라 -> 인접 리스트
# 플로이드 워셜 알고리즘 -> 인접 행렬 이용

# 항상 메모리와 시간을 염두에 두고 알고리즘을 선택해서 구현해야 함
# 최단 경로 문제에서 노드의 개수가 적은 경우에는 플로이드 워셜 알고리즘 이용
# 노드와 간선의 개수가 많으면 우선순위 큐를 이용하는 다익스트라 알고리즘을 이용하면 유리함

# 서로소 집합
# 공통 원소가 없는 두 집합 ex) 집합 {1, 2}와 {3, 4}는 서로소 관계
# 서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# union과 find의 연산으로 조작 가능

# 1. union 연산을 확인하여 서로 연결된 두 노드 A, B를 확인
# - A와 B의 루트 노드 A', B'를 각각 찾는다.
# - A'를 B'의 부모노드로 설정한다(B'가 A'를 가리키도록 한다).
# 2. 모든 union 연산을 처리할 때까지 1의 과정을 반복한다.


# 구현
# def find_parent(parent, x):
#     # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# 경로 압축
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

