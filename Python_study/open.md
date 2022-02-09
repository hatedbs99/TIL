# open

open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.

| mode | 설명                      |
| :--- | :------------------------ |
| w    | 쓰기 모드로 파일 열기     |
| r    | 읽기 모드로 파일 열기     |
| a    | 추가 모드로 파일 열기     |
| b    | 바이너리 모드로 파일 열기 |

b는 w, r, a와 함께 사용한다.

```python
>>> f = open("binary_file", "rb")
```

위 예의 rb는 "바이너리 읽기 모드"를 의미한다.

다음 예의 fread와 fread2는 동일한 방법이다.

```python
>>> fread = open("read_mode.txt", 'r')
>>> fread2 = open("read_mode.txt")
```

즉 모드 부분을 생략하면 기본값으로 읽기 모드 r를 갖게 된다.

다음은 추가 모드(a)로 파일을 여는 예이다.

```python
>>> fappend = open("append_mode.txt", 'a')
```