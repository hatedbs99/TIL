# collections.deque

### 1. deque란

Deque(데크)는 **double-ended queue** 의 줄임말로, 앞과 뒤에서 즉, 양방향에서 데이터를 처리할 수 있는 queue형 자료구조를 의미한다. 아래의 [그림1]은 `deque`의 구조를 나타낸 그림이다.

![image-20210820044950023](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20210820044950023.png)

`python`에서 `collections.deque`는 `list`와 비슷하다. `list`의 `append(), pop()`등의 메소드를 `deque`에서도 제공한다. 예제 소스코드들을 통해 `list`와 `deque`의 차이를 알아보도록 하자. `collections.deque`의 자세한 설명은[docs.python.org](https://docs.python.org/3/library/collections.html#collections.deque)에서 확인할 수 있다.



### 2. collections.deque의 메소드(method)들

`collections.deque`의 메소드들 중 `list`와 차이를 보이는 메소드들 위주로 살펴 보도록 한다. 전체 메소드들은 [docs.python.org](https://docs.python.org/3/library/collections.html#collections.deque)에서 확인할 수 있다.



#### 1) append(x)

`list.append(x)`와 마찬가지로 x를 `deque`의 오른쪽(마지막)에 추가(삽입)해준다.

```python
# 예제1. list.append() vs deque.append()
import collections
# list
lst = ['a', 'b', 'c']
lst.append('d')
print(lst)
'''
결과
['a', 'b', 'c', 'd']
'''
# collections.deque
deq = collections.deque(['a', 'b', 'c'])
deq.append('d')
print(deq)
'''
결과
deque(['a', 'b', 'c', 'd'])
'''
```



#### 2) appendleft(x)

앞에서 설명했다시피, `deque`는 양방향에서 데이터를 처리할 수 있는 구조이다. 따라서, `append(x)`가 오른쪽에서 추가(삽입)을 해준다면, `appendleft(x)`는 왼쪽 즉, 앞쪽에서 x를 추가(삽입)해주는 메소드이다.

```python
# 예제2. deque.appendleft()
import collections
deq = collections.deque(['a', 'b', 'c'])
deq.appendleft('d')
print(deq)
'''
결과
deque(['d', 'a', 'b', 'c'])
'''
```



#### 3) extend(iterable)

`list.extend(iterable)`과 마찬가지로 `iterable argument(list, str, tuple...)`를 오른쪽(마지막)에 `elements`를 추가(삽입)해주는 메소드이다. (*iterable argument* 는 arguments의 각 요소를 하나씩 반환 가능한 object를 의미한다.) [예제3-2]는 `append vs extend`의 차이를 나타낸 예제이다.

```python
# 예제3-1. list.append() vs deque.append()
import collections
# list
lst = ['a', 'b', 'c']
lst.extend('d')
print(lst)
'''
결과
['a', 'b', 'c', 'd']
'''
# collections.deque
deq = collections.deque(['a', 'b', 'c'])
deq.extend('d')
print(deq)
'''
결과
deque(['a', 'b', 'c', 'd'])
'''
# 예제3-2. append() vs extend()
lst2 = ['a', 'b', 'c', 'd']
lst2.append('ef') # append()
lst.extend('ef') # extend()
print("lst.extend('ef') >> ", lst)
print("lst2.append('ef') >>", lst2)
'''
결과
lst.extend('ef') >> ['a', 'b', 'c', 'd', 'e', 'f']
lst2.append('ef') >> ['a', 'b', 'c', 'd', 'ef']
```



#### 4) extendleft(iterable)

`collections.deque.extendleft()`는 `appendleft()`와 마찬가지로 왼쪽(앞쪽)에서 데이터를 추가해주는 메소드이다.

```python
# 예제4. extendleft()
import collections
deq = collections.deque(['a', 'b', 'c'])
deq.extendleft('de')
print(deq)
'''
결과
deque(['e', 'd', 'a', 'b', 'c'])
'''
```



#### 5) pop()

`list.pop()`과 같이 오른쪽(마지막)에서 부터 차례대로 제거와 반환(*remove and return*)을 하는 메소드이다.

```python
# 예제5. list.pop() vs deque.pop()
import collections
lst = ['a', 'b', 'c']
print('list.pop() ->', end=' ')
while True:
    try:
        print(lst.pop(), end=' ')
    except IndexError:
    	break
    print()
    deq = collections.deque(['a', 'b', 'c'])
    print('deque.pop() ->', end=' ')
while True:
    try:
    	print(deq.pop(), end=' ')
    except IndexError:
    	break
'''
결과
list.pop() -> c b a
deque.pop() -> c b a
'''
```

#### 6) popleft()

`pop()`의 반대로, 왼쪽(앞쪽)에서 부터 차례대로 제거와 반환(*remove and return*)을 하는 메소드이다.

```python
# 예제6. deque.popleft()
import collections
deq = collections.deque(['a', 'b', 'c'])
print('deque.popleft() ->', end=' ')
while True:
try:
print(deq.popleft(), end=' ')
except IndexError:
break
'''
결과
deque.popleft() -> a b c
'''
```

#### 7) rotate(n)

`collections.deque.rotate(n)`은 요소들(elements)을 n값 만큼 회전 해주는 메소드이다. n의 값이 음수(negative)이면 왼쪽으로 회전하고, n의 값이 양수이면 오른쪽으로 회전한다.

```python
# 예제7. rotate(n)

import collections

deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(1)
print('deq  >>', ' '.join(deq))

deq2 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq2.rotate(2)
print('deq2 >>', ' '.join(deq2))

deq3 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq3.rotate(-1)
print('deq3 >>', ' '.join(deq3))

deq4 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq4.rotate(-2)
print('deq4 >>', ' '.join(deq4))

'''
결과
deq  >> e a b c d
deq2 >> d e a b c
deq3 >> b c d e a
deq4 >> c d e a b
'''	
```



출처: https://excelsior-cjh.tistory.com/96 [EXCELSIOR]