from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.pop() # 3
print(queue)
queue.pop() # 2
print(queue)
queue.pop() # 1
print(queue)

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft() # 1
print(queue)
queue.popleft() # 2
print(queue)
queue.popleft() # 3
print(queue)