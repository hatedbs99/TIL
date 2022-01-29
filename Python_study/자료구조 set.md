# 자료구조 set

#### 1. set 특징

- 셋은 값은 없고 키만 있는 딕셔너리와 같다

- 딕셔너리와 마찬가지로 셋 또한 각 키는 유일해야 한다

- 순서는 보장되지 않는다

- 어떤 것이 존재하는지 여부만 판단하기 위해 셋을 사용한다
  반대로 키에 어떤 정보를 첨부하고 싶다면 딕셔너리를 사용한다

  

#### 2. set 생성

- set() 함수로 셋 생성

- 중괄호 {} 안에 콤마로 구분된 하나 이상의 값으로 셋 생성

  ```python
  ### 셋 생성 ###
  setVariable = set()
  print(type(setVariable))   # <class 'set'>
  print(setVariable)         # set()
   
  setVariable = {1,2,3,4,5}
  print(type(setVariable))   # <class 'set'>
  print(setVariable)         # {1, 2, 3, 4, 5}
   
  ### dict 생성 - set과 비교 ###
  dictVariable = {'a': 1, 'b': 2, 'c': 3}
  print(type(dictVariable))   # <class 'dict'>
  print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3}
  ```



#### 3. set 변환

set() 함수를 통해 문자열, 리스트, 튜플, 딕셔너리로부터 중복된 값은 없어진 상태로(하나의 키값으로 덮어진 상태로) 생성

- 문자열을 셋으로 변환

  ```python
  ### set 변환 - 문자열 to 셋 ###
  stringVar = "message"
  setVariable = set(stringVar)
  print(type(setVariable))        # <class 'set'>
  print(setVariable)              # {'g', 's', 'e', 'm', 'a'}
  ```

- 리스트를 셋으로 변환

  ```python
  ### set 변환 - 리스트 to 셋 ###
  listVar = ['a1', 'b2', 'c3', 'd4']
  setVar = set(listVar)
  print(type(setVar))        # <class 'set'>
  print(setVar)              # {'c3', 'd4', 'b2', 'a1'}
  ```

- 튜플을 셋으로 변환

  ```python
  ### set 변환 - 튜플 to 셋 ###
  tupleVar = ('a1', 'b2', 'c3', 'd4')
  setVar = set(tupleVar)
  print(type(setVar))        # <class 'set'>
  print(setVar)              # {'c3', 'd4', 'a1', 'b2'}
  ```

- 딕셔너리를 셋으로 변환(set()을 사용하면 딕셔너리의 키 값만 사용)

  ```python
  ### set 변환 - 딕셔너리 to 셋 ###
  dictVar = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  setVar = set(dictVar)
  print(type(setVar))        # <class 'set'>
  print(setVar)              # {'b', 'd', 'a', 'c'}
  ```



#### 4. set 항목 추가

```python
### 셋 항목 추가 ###
A_food = {'면', '스프', '물', '계란'}
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '스프', '면', '계란'}
A_food.add('대파')
A_food.add('고추')
print(type(A_food))     # <class 'set'>
print(A_food)           # {'고추', '대파', '계란', '면', '스프', '물'}
```



#### 5. set 항목 결합

```
### 셋 항목 결합 ###
A_food = {'면', '스프', '물', '계란'}
print(type(A_food))         # <class 'set'>
print(A_food)               # {'물', '스프', '면', '계란'}
 
B_food = {'대파', '고추'}   # <class 'set'>
A_food.update(B_food)
print(type(A_food))         # <class 'set'>
print(A_food)               # {'물', '대파', '고추', '면', '계란', '스프'}
 
C_food = ['치즈', '떡', '김치'] # <class 'list'>
A_food.update(C_food)
print(type(A_food))         # <class 'set'>
print(A_food)               # {'계란', '고추', '떡', '치즈', '물', '면', '대파', '김치',
							# '스프'}
```



#### 6. set 항목 삭제

```python
### 셋 항목 삭제 ###
# remove
A_food = {'면', '스프', '물', '계란'}
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '스프', '면', '계란'}
A_food.remove('계란')
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '스프', '면'}
A_food.remove('계란')   # KeyError: '계란'
 
# discard
A_food = {'면', '스프', '물', '계란'}
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '스프', '면', '계란'}
A_food.discard('계란')
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '스프', '면'}
A_food.discard('계란')
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '스프', '면'}
```

- remove()메서드로 삭제 후 다시 삭제하려할때, 해당 값이 존재하지 않는 상태라면 KeyError 발생한다
- discard()메서드는 remove()와는 반대로 없는 값을 삭제하더라도 에러가 발생하지 않는다



#### 7. set 항목 복사

```python
### 셋 항목 복사 ###
A_food = {'면', '스프', '물', '계란'}
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '면', '계란', '스프'}
B_food = A_food.copy()
print(type(B_food))     # <class 'set'>
print(B_food)           # {'물', '면', '계란', '스프'}
 
A_food.discard('계란')
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '면', '스프'}
print(type(B_food))     # <class 'set'>
print(B_food)           # {'물', '면', '계란', '스프'}
```



#### 8. set 콤비네이션과 연산자

+ in으로 값 확인하기

  ```python
  foods = {
      '라면' : {'면', '스프', '물', '계란'},
      '김치찌개' : {'물', '김치', '고기'},
      '부대찌개' : {'물', '스팸', '고기', '면'},
      '된장찌개' : {'물', '된장', '두부'}
  }
   
  for food, list in foods.items():
      if '물' in list:
          print(food)
          # 라면
          # 김치찌개
          # 부대찌개
          # 된장찌개
  ```

  + foods 딕셔너리 안에 키는 라면, 김치찌개, 부대찌개, 된장찌개이고 값은 셋으로 구성되어 있다
  + items 메서드를 통해 키-값을 가져온 후 '물'을 구성하는 음식을 출력한다

+ 인터섹션 연산자 (교집합 : 양쪽 셋에 모두 들어 있는 멤버, &, intersection())

  ```python
  foods = {
      '라면' : {'면', '스프', '물', '계란'},
      '김치찌개' : {'물', '김치', '고기'},
      '부대찌개' : {'물', '스팸', '고기', '면'},
      '된장찌개' : {'물', '된장', '두부'}
  }
   
  for food, list in foods.items():
      if list & {'고기', '면'}:
          print(food)
          # 라면
          # 김치찌개
          # 부대찌개
  ```

  - 고기, 면이 포함된 (교집합이 된) 음식을 출력
  - 고기, 면이 포함되어 있기때문에 True를 리턴하게 되고 해당 food가 출력된다

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food & B_food))    # <class 'set'>
  print(A_food & B_food)          # 물, 면
  print(type(A_food.intersection(B_food)))    # <class 'set'>
  print(A_food.intersection(B_food))          # 물, 면
  ```

  + A_food 와 B_food 에서 겹쳐지는(교집합, intersection) 멤버 값 출력

+ 유니온 (합집합 : 각 셋의 모든 멤버, |)

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food | B_food))    # <class 'set'>
  print(A_food | B_food)          # {'면', '스팸', '스프', '물', '계란', '고기'}
  ```

+ 디퍼런스 (차집합 : 첫번째 셋에는 있지만 두번째 셋에서는 없는 멤버, -)

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food - B_food))    # <class 'set'>
  print(A_food - B_food)          # {'스프', '계란'}
  ```

+ 서브셋 (부분집합, <=, issubset())

  첫번째 셋이 두번째 셋의 서브셋(부분집합)인지 확인

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food <= B_food))    # <class 'bool'>
  print(A_food <= B_food)          # False
  print(type(A_food.issubset(B_food)))    # <class 'bool'>
  print(A_food.issubset(B_food))          # False
   
  A_food = {'면', '물'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food <= B_food))    # <class 'bool'>
  print(A_food <= B_food)          # True
  print(type(A_food.issubset(B_food)))    # <class 'bool'>
  print(A_food.issubset(B_food))          # True
  ```

+ 슈퍼셋 (상위 집합, >=, issuperset())

  서브셋의 반대, 첫번째 셋이 두번째 셋의 슈퍼셋인지 확인

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food >= B_food))    # <class 'bool'>
  print(A_food >= B_food)          # False
  print(type(A_food.issuperset(B_food)))    # <class 'bool'>
  print(A_food.issuperset(B_food))          # False
   
  A_food = {'물', '스팸', '고기', '면'}
  B_food = {'면', '물'}
  print(type(A_food >= B_food))    # <class 'bool'>
  print(A_food >= B_food)          # True
  print(type(A_food.issuperset(B_food)))    # <class 'bool'>
  print(A_food.issuperset(B_food))          # True
  ```

+ 프로퍼 서브셋 (진부분집합, <)

  프로퍼 서브셋(진부분 집합), 두번째 셋에는 첫번째 셋의 모든 멤버를 포함한 그 이상의 멤버가 있어야 함

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food < B_food))    # <class 'bool'>
  print(A_food < B_food)          # False
   
  A_food = {'면', '물'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food < B_food))    # <class 'bool'>
  print(A_food < B_food)          # True
  ```

+ 프로퍼 슈퍼셋 (진부분집합, >)

  첫번째 셋이 두번째 셋의 모든 멤버를 포함한 그 이상의 멤버가 있어야함

  ```python
  A_food = {'면', '스프', '물', '계란'}
  B_food = {'물', '스팸', '고기', '면'}
  print(type(A_food > B_food))    # <class 'bool'>
  print(A_food > B_food)          # False
   
  A_food = {'물', '스팸', '고기', '면'}
  B_food = {'면', '물'}
  print(type(A_food > B_food))    # <class 'bool'>
  print(A_food > B_food)          # True
  ```

  