# Using collections.deque as a FIFO queue

print("*** COLLECTIONS MODULE ***")
from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
# customQueue.append(4) overrides the first element from the opposite side
print(customQueue)
print(customQueue.popleft())
print(customQueue)
customQueue.clear()
print(customQueue)

print("*** QUEUE MODULE ***")
# can also be used for LIFO queue and Priority queue
# Has task_done and join method not shown below
import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.qsize())
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.qsize())
print(customQueue.get())
print(customQueue.qsize())

print("*** MULTIPROCESSING MODULE ***")
# multiprocessing.Queue as a FIFO queue.

from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.qsize())
print(customQueue.get())

