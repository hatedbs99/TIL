# zip 함수

### zip

zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환한다.

```python
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
    	print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
```



### 병렬 처리

zip()함수를 활용하면 여러 그룹의 데이터를 루프를 한 번만 돌면서 처리할 수 있다. 가변 인자를 받기 때문에 2개 이상의 인자를 넘겨서 병렬 처리를 할 수 있다.

```python
>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    	print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e
```



### unzip

zip()함수로 엮어 놓은 데이터를 다시 해체(unzip)하고 싶을 때도 zip()함수를 사용할 수 있다.

2개의 튜플 데이터를 엮은 후 리스트로 변환 예제

```python
>>> numbers = (1, 2, 3)
>>> letters = ("A", "B", "C")
>>> pairs = list(zip(numbers, letters))
>>> pairs
[(1, 'A'), (2, 'B'), (3, 'C')]
```

이 리스트 앞에 풀기(unpacking) 연산자 붙여서 다시 zip()함수에 넘기면 다시 원래 2개의 튜플을 얻을 수 있다.

```python
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3)
>>> letters
('A', 'B', 'C')
```



### 사전 변환

zip()함수를 이용하면 두 개의 리스트나 튜플 부터 쉽게 dictionary를 만들 수 있다.

키를 담고 있는 리스트와 값을 담고 있는 리스트를 zip()함수에 넘긴 후 그 결과를 다시 dict()함수에 넘기면 된다.

```python
>>> keys = [1, 2, 3]
>>> values = ["A", "B", "C"]
>>> dict(zip(keys, values))
{1: 'A', 2: 'B', 3: 'C'}
```

dict()함수에 키와 값으로 이루어진 튜플을 넘기면 사전이 생성되는 원리를 이용한 것.

날짜 데이터의 필드 이름 리스트와 필드 값 리스트를 사전으로 변환 예제

```python
>>> dict(zip(["year", "month", "date"], [2001, 1, 31]))
{'year': 2001, 'month': 1, 'date': 31}
```



### 주의 사항

zip()함수로 넘기는 인자의 길이가 다를 때는 주의해야 한다. 가장 짧은 인자를 기준으로 데이터가 엮이고, 나머지는 버려지기 때문.

```python
>>> numbers = ["1", "2", "3"]
>>> letters = ["A"]
>>> list(zip(numbers, letters))
[('1', 'A')]
```

