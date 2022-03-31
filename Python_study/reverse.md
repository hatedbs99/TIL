# reverse

#### 1. reverse

reverse는 list 타입에서 제공하는 함수이다.

기본형 : list.reverse()

```python
l = ['a', 'b', 'c'] # list타입
t = ('a', 'b', 'c') # tuple타입
d = {'a': 1, 'b': 2, 'c': 3} # dictionary타입
s = 'abc' # string 타입

l.reverse()
t.reverse()
d.reverse()
s.reverse()

print(l[:])

# result
['c', 'b', 'a']

```



리스트 값을 반환하는 것이 아니라 변환시켜줌으로써

print(l.reverse())는 None으로 출력됨



```python
l = ['a', 'b', 'c']
l_reverse = l.reverse()

print(l_reverse)  
print(l) 

-------------------------------
# result

None
['c', 'b', 'a']
```



#### 2. reversed

reversed는 내장함수로, list에서 제공하는 함수가 아니다.

기본형 = reverse(var)

```python
l = [' t', 'o', 'p'] # list타입
t = ('t', 'o', 'p') # tuple 타입
d = {'t': 1, 'o': 2, 'p': 3} # dict 타입
s = 'top' # string 타입

reversed(l)  # <listreverseiterator object at 0x101053c10>
reversed(t)  # <reversed object at 0x101053b50>
reversed(d)  # TypeError: argument to reversed() must be a sequence
reversed(s)  # <reversed object at 0x101053c10>

print(reversed(l))  
print(reversed(t))  
print(reversed(s))  
-------------------------------------------------
# result
<list_reverseiterator object at 0x0000019540D7A130>
<reversed object at 0x0000019540D7A130>
<reversed object at 0x0000019540D7A130>
```

딕셔너리는 순서가 있는 타입이 아니므로 지원하지 않는다.

또한 print를 하였을때 속성값이 나온다.

변환된 값을 출력하고싶을때는

아래와 같이

```python
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
s = 'abc'

list_1 = list(reversed(l))  # ['c', 'b', 'a']
tuple_1 = tuple(reversed(t))  # ('c', 'b', 'a')
string = str(reversed(s))
string_list = list(reversed(s))
string_tuple = tuple(reversed(s))



print(list_1)
print(tuple_1)
print(string)
print(string_list)
print(string_tuple)

-------------------------------------------------
# result

['c', 'b', 'a']
('c', 'b', 'a')
<reversed object at 0x000002E2699BA130>
['c', 'b', 'a']
('c', 'b', 'a')

# string을 변환하기 위해서 는 다른 방법이 필요하다
str = 'abc'
reversed_str = "".join(reversed(str))
print(reversed_str)

# result
'cba'
```



