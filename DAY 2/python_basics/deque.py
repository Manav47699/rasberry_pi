# doubly ended queue

from collections import deque

queue = deque([1, 2, 4])

print (queue)
queue.append(100)
print(queue)
queue.appendleft(200)
print(queue)
queue.popleft()            
print(queue)



while queue:
    val = queue.pop()
    print(val)