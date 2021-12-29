class ListNode:
    def __init__(self, x=0, next=None) -> None:
        self.val = x
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        # 合并后l1和l2
        prev.next = l1 if l1 is not None else l2

        return prehead.next
