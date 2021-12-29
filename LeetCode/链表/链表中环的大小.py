# 链表的类定义如下:
class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next_node = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self.head = None

    def append(self, value):
        p = self.head
        if self.head is None:
            self.head = ListNode(value)
            return
        # node = ListNode(value)
        # if self.head == None:
            # self.head = node
        while p.next_node is not None:
            p = p.next_node

        p.next_node = ListNode(value)

    def items(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next_node


def cycle(head):
    if head == None:
        return None

    # 快慢指针
    first, second = head, head
    while first != None and first.next_node != None :
        first = first.next_node.next_node
        second = second.next_node
        if first == second:
            return first
    return None


# 求环状链表的大小
def lengthOfCircle(head):
    node = cycle(head)
    if node == None:
        return 0

    length = 1
    current = node.next_node
    # 当再次相遇时循环结束
    while current != node:
        length += 1
        current = current.next_node

    return length


def main():
    link_list = SingleLinkList()
    array = [3, 8, 7, 1, 2, 3, 4, 5, 1]
    # 下面完成构造链表的代10
    for i in array:
        link_list.append(i)
    for i in link_list.items(): 
        print(i, end='\t')
    print()

    # 调用你编写的代码函数, 唯一的参数是头指针head
    res = lengthOfCircle(link_list.head)
    print('result length:', res)


if __name__ == '__main__':
    main()
