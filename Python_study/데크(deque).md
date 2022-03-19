# 데크(deque)

보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면에 양뱡향 큐가 있는데 그것이 바로 데크(deque)이다.

즉, 앞뒤 양쪽 방향에서 엘리먼트를 추가하거나 제거할 수 있다.

데크는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.

컨테이너의 양 끝 엘리먼트에 접근하여 삽입 또는 제거를 할 경우, 일반적인 리스트가 이러한 연산에 O(n)이 소요되는데에 반해, 데크는 O(1)로 접근 가능하다.



#### deque 사용법

```python
from collections import deque

dq = deque()

# 왼쪽에 10 삽입
dq.appendleft(10)

# 오른쪽에 0 삽입
dq.append(0)

# 왼쪽 끝 엘리먼트를 가져오며 데크에서 삭제
dq.popleft()

# 오른쪽 끝 엘리먼트를 가져오며 데크에서 삭제
dq.pop()
```

데크(deque)에 존재하는 메서드(method)는 대략 다음과 같다.

- `deque.append(item)`: item을 데크의 오른쪽 끝에 삽입한다.
- `deque.appendleft(item)`: item을 데크의 왼쪽 끝에 삽입한다.
- `deque.pop()`: 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- `deque.popleft()`: 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- `deque.extend(array)`: 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- `deque.extendleft(array)`: 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- `deque.remove(item)`: item을 데크에서 찾아 삭제한다.
- `deque.rotate(num)`: 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
- `deque.index(item)`: item의 index를 출력한다.



```python
dq = deque([1, 2, 3, 4, 5])

dq.rotate(1)
print(dq)
>>> deque([5, 1, 2, 3, 4])

dq.rotate(-1)
print(dq)
>>> deque([1, 2, 3, 4, 5])
```

rotate메서드를 이용하면 데크를 좌우로 회전할 수 있다.



#### 언제 데크를 사용해야 하는가?

데크는 스택처럼 사용할수도, 큐처럼 사용할 수도 있다.

시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 뺄 때 사용하면 최적화된 연산 속도를 제공한다.