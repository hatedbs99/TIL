# join 함수



함수의 모양은 다음과 같다.

''.join(리스트)

'구분자'.join(리스트)



join 함수는 매개변수로 들어온 리스트에 있는 요소를 모두 합쳐 하나의 문자열로 반환하는 함수이다.



#### ''.join(리스트)

매개변수로 들어온 ['a', 'b', 'c', 'd']와 같은 리스트를 'abcd'의 문자열로 반환해 주는 함수이다.



#### '구분자'.join(리스트)

리스트의 값들 사이에 '구분자'에 들어온 구분자를 넣어 하나의 문자열로 반환해준다.

'.'.join(['www', 'naver', 'com'])을 예로 들면 'www.naver.com' 형태로 문자열을 만들어 반환해준다.



#### int형 리스트를 join 하는 경우

```python
num_list = [-1, 0, 1, 3, 4, 5, 9]

print(num_list)
# [-1, 0, 1, 3, 4, 5, 9]
print(" ".join(map(str, num_list)))
# -1 0 1 3 4 5 9

# print(" ".join(num_list))
# TypeError: sequence item 0: expected str instance, int found
```