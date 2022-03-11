# if \_\_name\_\_ == "_\_main__"의 의미

```python
if __name__ == "__main__"
```

파이썬에서 이러한 조건문이 자주 등장한다. 이 조건문은 현재 코드가 프로그램의 진입점 entry point 또는 main인지를 체크하는 부분이다.



#### \_\_name\_\_변수

모듈의 이름을 출력해주는 기능을 한다. 하지만 현재 코드가 프로그램의 진입점 entry point인 경우에는 \_\_main\_\_이라는 값을 가지게 된다.

```python
# main.py 
import external_module 
print("It's main.py") 
print(__name__) 


#external_module.py 
print("It's external_module.py") 
print(__name__) 
```





```python
# main.py 
import external_module 
print(square(10) 


#external_module.py 
def square(n): 
	return n*n 

print("square(10) :" + square(10)) 
```

external_module 부분에 square함수의 사용법을 출력하는 코드가 있을 때 이를 main에서 활용하면 해당 코드도 함께 출력된다. 하지만 external_module을 모듈로 사용하는 사람들이 해당 모듈을 사용할 때도 해당 코드는 계속 동작한다.



```python
#external_module.py 
def square(n): 
	return n*n 

if __name__ == "__main__": 
	print("square(10) :" + square(10))
```

위와 같이 조건문을 넣으면 main함수로 사용할 때에만 해당 코드를 출력하게 만들 수 있다.