from collections import deque


queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

print(queue)


a = queue.popleft()
print(a)
queue.append(1)
queue.append(4)

queue.popleft()

print(queue)
queue.reverse()
print(queue)
queue = list(queue)

print(queue)
