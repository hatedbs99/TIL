# enumerate()

```python
>>> for entry in enumerate(['A', 'B', 'C'])
		print(entry)

(0, 'A')
(1, 'B')
(2, 'C')

# 시작 index 변경
>>> for entry in enumerate(['A', 'B', 'C'], start=1)
		print(entry)

(1, 'A')
(2, 'B')
(3, 'C')
```

