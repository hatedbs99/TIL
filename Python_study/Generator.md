### Generator

- `Generator(제너레이터)`: `iterator` 를 생성해 주는 함수

  - `iterator` : `next()` 메서드를 이용해 데이터에 순차적으로 접근이 가능한 객체

- `generator` 는 일반적인 함수와 비슷해보이지만, 가장 큰 차이점은 `yield` 라는 구문일 것이다. 아래의 예시를 보자

  ```python
  def generator(n):
      i = 0
      while i < n:
          yield i
          i += 1
  ```

  일반 함수와의 차이는 `yield` 밖에 없다. `yield`는 무엇인가?

  - `yield` 는 `generator`가 일반 함수와 구분되는 가장 핵심적인 부분이다.

  - 일반적인 함수의 경우, 사용이 종료되면 결과 값을 호출부로 반환한 뒤 함수 자체를 종료시킨 후 메모리 상에서 정리(clear)된다.

  - 하지만, `yield`는 다르다. `generator` 함수가 실행 중에 `yield`를 만날 경우, 해당 함수는 그 상태로 정지되며, 반환 값을 `next()`를 호출한 쪽으로 전달한다. 이후 해당 함수는 일반적인 경우처럼 종료되는 것이 아니라 그 상태로 유지되게 된다. *즉, 함수에서 사용된 로컬 변수나 `instruction pointer` 등과 같은 함수 내부에서 사용된 데이터들이 메모리에 그대로 유지된다.*

    

    ```python
    def generator(n):
        i = 0
        while i < n:
            yield i
            i += 1
    
    for x in generator(5):
        print(x)
    
    # 출력
    0
    1
    2
    3
    4
    ```

    위 구문을 하나씩 살펴보자.

    1. for 문이 실행되며 `generator` 함수가 호출된다.
    2. `generator` 함수는 일반 함수와 동일한 절차로 실행된다.
    3. 실행 중 while 문 안에서 `yield`를 만나게 된다. 그러면 return 과 비슷하게 함수를 호출했던 구문으로 반환하게 된다. 여기서는 첫번째 i 값인 0을 반환한다. *하지만 반환했다고 `generator` 함수가 종료되는 것이 아니라 그대로 유지한 상태이다.*
    4. x 값에는 `yield`에서 전달된 0 값이 저장된 후 출력된다. 그 후 for 문에 의해 다시 `generator` 함수가 호출된다.
    5. 이 때, `generator` 함수는 처음부터 시작되는 것이 아니라 `yield` 이후부터 시작된다. 따라서 `"i += 1"` 문장이 실행되고 i 값은 1로 증가한다.
    6. 아직 while 문 내부이기 때문에 `yield` 구문을 만나 i 값인 1이 전달된다.
    7. x 값은 1을 전달 받고 출력된다. (이후 반복)