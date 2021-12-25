from collections import deque

queue = deque()

queue.append(3)
queue.append(1)
queue.append(5)
queue.append(2)
queue.popleft()
queue.append(3)
queue.append(10)
queue.append(9)
queue.popleft()

print(queue) # 처음부터 출력
queue.reverse() # 역순으로 변경
print(queue)
list(queue) # 리스트 자료형으로 변경