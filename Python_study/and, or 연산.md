# and, or 연산

bool타입도 연산이 가능하다.

파이썬은 참과 거짓을 반드시 bool객체, 즉 True와 False의 형태로만 취급하지 않는다.

거짓으로 취급되는 형태 숫자 0, 비어있는 문자열 등 거짓으로 취급되는 객체는 그 자체가 False이다.



### and

and 연산자는 다음과 같이 사용 가능하다.

A and B

and 연산자 앞 뒤에 객체(혹은 결과가 객체인 연산)가 참인 경우에는 True, 둘 중 하나만 참인 경우, 혹은 둘 다 거짓인 경우에는 False를 리턴한다.

```python
>>> '' and True
''
>>> 0 and True
0
>>> False and True
False
```

```python
>>> True and ''
''
>>> True and 1 + 2 + 3 * 0
3
>>> True and 'False'
'False'
```

### or

둘 중 하나만 참이라도 True를 리턴해주는 연산

표현식1 or 표현식2 로 사용



표현식 1이 참이라면 뒤의 표현식은 신경 쓰지 않고 표현식 1을 리턴해준다.

```python
>>> 1 or ''
1
```

표현식 1이 거짓이라면 표현식2는 신경 쓰지 않는다. 어차피 결정은 표현식 2가 참이냐 거짓이냐에 따라 달려있다. 따라서 표현식 2의 계산결과를 리턴해준다.

```python
>>>  0 or 1 * 2 * 3 * 0
0
>>> False or 'False'
'False'
```



### not

not은 특정 표현식의 반대 값을 리턴해준다.

결과값은 항상 True, False 객체이다.

```python
>>> not 0
True
>>> not 1
False
>>> not 'False'
False
```

