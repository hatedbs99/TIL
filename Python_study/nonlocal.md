# nonlocal

#### 1. nonlocal 예제

```python
def stackAdd():
    totalValue = 0
    stackCount = 0
    def add(value):
        stackCount += 1
        totalValue += value
        return totalValue, stackCount
    return add
 
add = stackAdd()
print(add(3))   # UnboundLocalError: local variable 'stackCount' referenced
				# before assignment
print(add(2))
```

- 어떻게 보면 add() 함수안에 stackCount, totalValue가 stackAdd()함수안에있는 자유변수를 참조해서 연산이 가능하다고 생각할 수 있다
- add()함수 내부를 다시보면, stackCount+=1 는 stackCount = stackCount + 1와 같은데, 함수 안에서 stackCount변수를 할당하고있으므로 지역변수로 만들어버린다(totalValue도 마찬가지)
- 전에 [클로저(closure)](https://www.byfuls.com/programming/read?id=38)에서는 menu라는 리스트 변수도 이와 비슷하지만, menu리스트 자체에 할당하지 않았고 메서드를 활용했기에 이와 같은 문제가 발생하지 않았다
- 숫자, 문자열, 튜플 등 불변형은 읽을 수만 있고 값은 갱신할 수 없다
- stackCount = stackCount + 1과 같이 변수를 다시 바인딩하면 암묵적으로 stackCount라는 지역변수를 할당한다
- stackCount는 지역변수이므로 자유변수가 아니기에 클로저에 해당하지 않는다



```python
def stackAdd():
    totalValue = 0
    stackCount = 0
    def add(value):
        nonlocal totalValue, stackCount
        stackCount += 1
        totalValue += value
        return totalValue, stackCount
    return add
 
add = stackAdd()
print(add(3))   # (3, 1)
print(add(2))   # (5, 2)
```

- add함수 안에 nonlocal 키워드를 선언했다
- nonlocal 선언하면 함수 안에서 변수에 새로운 값을 할당하더라도 그 변수는 자유변수임을 나타낸다
- 새로운 값을 nonlocal 변수에 할당하면 클로저에 저장된 바인딩이 변경된다