"""
FIFO = First In, First Out
"""
from collections import deque

#initialisation de la file(vide)
file = deque()

# enqueue 1
file.append(1)
# enqueue 2
file.append(2)

print(file)
# dequeue 1
print(file.popleft())
# dequeue 2
print(file.popleft())
