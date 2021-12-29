# 请定义一个队列并实现函数 max_value 得到队列里的最大值，
# 要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

# 若队列为空，pop_front 和 max_value 需要返回 -1
import queue


class MaxQueue:

    def __init__(self):
        # 初始化双端队列
        self.deque = queue.deque()

    def max_value(self) -> int:
        # 双向队列求最大值使用max(self.deque)，类似于list
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        # 入队列，使用append，类似于list
        self.deque.append(value)

    def pop_front(self) -> int:
        # 出队列(从左侧出)，即popleft方法
        return self.deque.popleft() if self.deque else -1
