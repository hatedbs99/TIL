# lambda

lambda 키워드들 사용해서 작고 이름 없는 함수를 만들 수 있다. 이 함수는 두 인자의 합을 돌려준다.: `lambda a, b: a+b`. 함수 객체가 있어야 하는 곳이면 어디나 람다 함수가 사용될 수 있다. 문법적으로는 하나의 표현식으로 제한된다. 의미적으로는, 일반적인 함수 정의의 편의 문법일 뿐이다. 중첩된 함수 정의처럼, 람다 함수는 둘러싸는 스코프에 있는 변수들을 참조할 수 있다:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

위의 예는 함수를 돌려주기 위해 람다 표현식을 사용한다. 또 다른 용도는 작은 함수를 인자로 전달하는 것이다:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

