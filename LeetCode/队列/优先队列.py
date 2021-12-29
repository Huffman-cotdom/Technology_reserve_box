# 一般来说，优先级队列都是使用堆这种数据结构来实现。而heapq就是Python标准库中堆的实现。heapq默认情况下实现的是最小堆。
# 入队操作使用heappush()，出队操作使用heappop()。
import heapq
from queue import PriorityQueue

q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

print(q)

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# queue.PriorityQueue内部封装了heapq，不同的是它是线程安全的。在并发环境下应该选择使用PriorityQueue。
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
