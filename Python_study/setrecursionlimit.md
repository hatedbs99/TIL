# setrecursionlimit



```python
import sys
sys.setrecursionlimit(10 ** 6)
```

재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 써야한다. 파이썬의 기본 재귀 깊이제한은 1000으로 매우 얕은 편이다. 따라서 재귀로 문제를  풀 경우, 이 제한에 걸리게 된다. 이 때, sys.setrecursionlimit(10 ** 6)을 작성해주면 재귀의 최대 깊이가 10**6으로 바뀌게 된다.

