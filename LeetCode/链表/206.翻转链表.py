# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverseList(self, head):
        # # 定义尾部节点，默认为None
        # last = None
        # # 当传入的头部节点不为None时，即没有反转完成时
        # while head:
        #     # 连续赋值，等效于：将等号右边的变量全部暂存为中间变量, 再赋值给右侧，顺序从左至右
        #     # eg: l = last, h = head, hn = head.next, head.next = l, last = h, head = hn
        #     # 按照反转链表的定义，反转后新链表的最后一个节点是当前的head节点，所以对于新链表head.next=None（last的默认值）
        #     # 而last是一直变动的，处理完新链表的尾部后，从head开始，所以有last=head
        #     # last的遍历过程在改变着链表，我们是使用head来限制其应该何时结束，因此head也应该逐次变化，直到head.next指向None
        #     # 因此head变化为：head = head.next
        #     head.next, last, head = last, head, head.next
        # return last

        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
