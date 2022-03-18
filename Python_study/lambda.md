# lambda

lambda는 무명함수라고 불리며 그 이름대로 이름 없는 함수를 작성할 때 사용한다.

예를 들어 아래의 예에서는 lambda식을 사용해서 '인수를 2제곱하여 반환하는 무명 함수'를 변수 a에 대입하고 있다.

```python
a = lambda x : x*x print(a(4)) #16
```





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





lambda가 사용된 sort함수를 살펴보자.

```python
dictionary = [['なら',3], ['かながわ',4], ['とうきょう',1], ['おおさか',2]]

print(dictionary) # [['なら', 3], ['かながわ', 4], ['とうきょう', 1], ['おおさか', 2]]

sortedDict = sorted(dictionary, key=lambda x: x[1])

print(sortedDict) # [['とうきょう', 1], ['おおさか', 2], ['なら', 3], ['かながわ', 4]]
```

위의 예에서 리스트의 2번째의 요소를 원래 순서대로 정렬하고 있다.

그것은 sort함수의 key에 '요소 x를 받고, x[1]를 돌려준다'라는 lambda식을 지정하고 있기 때문이다.

이것에 의해, sort함수는 리스트의 2번째의 요소를 key로 하여 정렬한다. 

이번에는 리스트의 첫 번째 요소를 key로 하여 정렬하는 것을 생각해보자.

첫 번째를 key를 하고 싶은 경우, lambda식에 리스트의 첫 번째를 반환하는 함수를 정의하면 될 것이므로, 아래와 같이 코드를 작성할 수 있다.

```python
dictionary = [['なら',3], ['かながわ',4], ['とうきょう',1], ['おおさか',2]]

print(dictionary) # [['なら', 3], ['かながわ', 4], ['とうきょう', 1], ['おおさか', 2]]

sortedDict = sorted(dictionary, key=lambda x: x[0])# <- x[0]に変更

print(sortedDict) # [['おおさか', 2], ['かながわ', 4], ['とうきょう', 1], ['なら', 3]]
```



#### sort 함수에 있어서 lambda식이란?

lambda식 자체는 굉장히 깊은 내용을 가진 개념이지만, sort함수내에서는 거의 공식과 같이 사용될 뿐이다.

그러므로 아래와 같이 암기해두면 될 것이다.

```python
sorted ([list 혹은 dic], key = lambda x: [key로 지정하고 싶은 요소])
```

