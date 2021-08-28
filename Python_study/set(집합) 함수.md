# set(집합) 함수

### 1. set(집합)

- set은 수학에서 이야기하는 집합과 비슷하다.
- 순서가 없고, 집합안에서는 unique한 값을 가진다.
- 그리고 mutable(변경 가능한) 객체이다.
- REPL(콘솔 화면에서 파이썬 구문을 입력하면 바로 결과를 반환하고 다시 입력할수 있는 도구)으로 여러가지를 확인해본다.
- 중괄호를 사용하는 것은 dictionary와 비슷하지만, key가 없다. 값만 존재한다.

```python
>>> s = {3, 5, 7}
>>> s
{3, 5, 7}
>>> type(s)
<class 'set'>
```



- set(집합) 내부 원소는 다양한 값을 함께 가질 수 있지만, mutable한 값은 가질수 없다.

```python
>>> s = {"1", 3, 5, (1,3)}
>>> s
{(1, 3), 5, 3, '1'}

>>> s = {"1", 3, 5, [1,3]}
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> s = {"1", 3, 5, {1,3}}
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

>>> s = {"1", 3, 5, {1:1,3:3}}
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
        
>>> s = {"1", 3, 5, frozenset([1,3,4])}
>>> s
{5, 3, '1', frozenset({1, 3, 4})}
```

### 2. set(집합) 선언

- list나 dict의 경우 대괄호나 중괄호로 선언할 수 있었지만, set은 dict타입과 동일한 중괄호를 사용하므로, 중괄호만으로는 생성할 수 없습니다.
- set 생성자를 이용한다.

```python
>>> s = {}
>>> type(s)
<class 'dict'>

>>> s = set()
>>> type(s)
<class 'set'>

>>> s
set()
```



- set 생성자에 iterable한 객체를 넣으면 변환하여 set을 만들어 준다.
- 물론 set생성자 없이 바로 중괄호 안에 값을 넣어도 된다.

```python
>>> s = set([1,3,5,7])
>>> s
{1, 3, 5, 7}
>>> p = {1, 3, 5, 7}
>>> p
{1, 3, 5, 7}
```



- 중복된 값은 자동으로 중복이 제거 된다.

```python
>>> s = {1, 5, 1, 1, 1, 3, 7}
>>> s
{1, 3, 5, 7}
```



- set(집합)은 순서가 없습니다. 어떤 값이 먼저 나올지 알 수 없습니다.

```python
>>> for i in {1, 2, 4, 8, 16,32}:
...     print(i)
... 
32
1
2
4
8
16
```



### 3. set(집합)의 in

- 다른 collection 타입과 동일하게 동작한다.

```python
>>> 2 in r
True
>>> 3 in r
False
>>> 3 not in r
True
```



### 4. set(집합)의 원소 추가

- 원소 추가는 `add` 메소드를 이용한다.

```python
>>> k = {100, 105}
>>> k.add(50)
>>> k
{105, 50, 100}
>>> k.add(12)
>>> k
{105, 50, 100, 12}
```



### 5. set(집합)의 update

- dictionary의 update는 여러값을 수정 또는 추가할때 사용했지만, set은 중복은 자동으로 제거되고 수정이라는 개념보다, 여러 데이터를 한번에 추가할 때 사용한다.

```python
>>> k = {1, 2, 3}
>>> k.update([3, 4, 5])
>>> k
{1, 2, 3, 4, 5}
```



### 6. set(집합)의 원소 제거

- remove(item) : item에 해당하는 원소를 제거하고, 없으면 KeyError 발생

```python
>>> k = {1, 2, 3}
>>> k.remove(3)
>>> k
{1, 2}
>>> k.remove(3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 3
```



- discard(item) : item에 해당하는 원소를 제거하고, 없어도 에러발생하지 않음

```python
>>> k = {1, 2, 3}
>>> k.discard(3)
>>> k
{1, 2}
>>> k.discard(3)
>>> k
{1, 2}
```



### 7. set(집합)의 복사

- set 내부의 값은 불변의 값만 들어올 수 있기때문에 얕은 복사와 깊은 복사의 구분이 필요 없을것 같지만 일단 set의 메소드인 copy는 얕은 복사에 해당한다.

```python
>>> s = {1, 3, 5}
>>> t = s.copy()
>>> s
{1, 3, 5}
>>> t
{1, 3, 5}
>>> id(s)
4334668264
>>> id(t)
4334666696
```



- dictionary 처럼 생성자로 복사할 수 있습니다.

```python
>>> s = {1, 3, 5}
>>> t = set(s)
>>> s
{1, 3, 5}
>>> t
{1, 3, 5}
>>> id(s)
4334666248
>>> id(t)
4334667144
```



### 8. set(집합) 연산 - 연산자

- `|` - 합집합 연산자

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a | b
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2, 3, 4, 5, 6, 7}
```

- `&` : 교집합 연산자

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a & b
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{3, 4, 5}
```

- `-` : 차집합 연산자

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a - b
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2}
```

- `|=, &=, -=, ^=` : `=` 과 조합함으로써 연산과 동시에 할당합니다.
- id 또한 변경되지 않습니다.

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> a |= b
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> b
{3, 4, 5, 6, 7}

>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> id(a)
4334668040
>>> a &= b
>>> a
{3, 4, 5}
>>> id(a)
4334668040
```



### 9. set(집합) - 연산메소드

- union - 합집합

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.union(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2, 3, 4, 5, 6, 7}
```

- intersection - 교집합

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.intersection(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{3, 4, 5}
```

- difference - 차집합

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.difference(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2}
```

- symmetric_difference : 대칭차집합 연산자(합집합 - 교집합)

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.symmetric_difference(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2, 6, 7}
```



### 10. set(집합) - 기타 메소드

- issubset : 부분집합 여부 확인

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {1, 2, 3}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
```

- issuperset : issubset과 반대 superset인지 확인

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {1, 2, 3}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
```

- isdisjoint : 교집합이 없으면 True, 있으면 False

```python
>>> a = {1, 2, 3}
>>> b = {4, 5, 6}
>>> a.isdisjoint(b)
True
>>> c = {1, 2, 3}
>>> d = {3, 4, 5}
>>> c.isdisjoint(d)
False
```

