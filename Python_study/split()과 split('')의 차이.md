# split()과 split('')의 차이



```python
string = "word1 word2  word3   word4    "

print(string.split())
> ['word1', 'word2', 'word3', 'word4']
# split()은 공백이 몇 개이건 상관 없이 무조건 1개로 보고 처리함

print(string.split(" "))
> ['word1', 'word2', '', 'word3', '', '', 'word4', '', '', '', '']
# split(" ")은 공백을 모두 각각의 공백으로 따로 처리함
```

추가적으로 split()은 공백만 처리하는 것이 아니라 '\t', '\n'도 처리해준다.