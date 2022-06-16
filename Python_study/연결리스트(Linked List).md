# 연결리스트(Linked List)

연결 리스트는 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로, 데이터를 저장하는 자료 구조이다. 데이터를 담고 있는 노드들이 연결되어 있는데, 노드의 포인터가 다음이나 이전의 노드와의 연결을 담당하게 된다.



### 노드 구현

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
       
```



### 연결리스트 구현

```python
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        
    # 헤더부터 탐색하여 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    
    # 모든 노드 값 출력하기
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
```



### 노드 인덱스 알아내기

```python
def get_node(self, index):
	cnt = 0
	node = self.head
	while cnt < index:
		cnt += 1
		node = node.next
    return node
```



### 삽입

```python
def add_node(self, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    node = self.get_node(index-1)
    next_node jjjjj= node.next
    node.next = new_node
    new_node.next = next_node
```

5 -> 12  -> 8 을 5 -> 6 -> 12 -> 8 로 만들기 위해서 인덱스 1자리인 12에 들어가기 위해 5 노드 위치를 파악하고, 그 다음 next에 6노드를 연결한다. 6의 next가 12가 연결되게끔 구현한다.



### 삭제

```python
def delete_node(self, index):
	if index == 0:
		self.head = self.head.next
		return
	node = self.get_node(index-1)
	node.next = node.next.next
```

삭제하는 것은 더 간단하다. 5 -> 6 -> 12 - > 8에서 삭제하고자 하는 index번째 노드의 전 노드를 찾아 바로 다음 노드가 될 것을 연결해주면 된다.



5 -> 12 -> 8 으로 5와 12 사이의 6을 삭제하고자 한다면, 5의 next를 12로 연결해주면 된다.

