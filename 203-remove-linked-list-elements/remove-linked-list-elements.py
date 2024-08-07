# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return 
        start = head
        pre = head
        while start:
            if start.val==val:
                if start == head:
                    head = head.next
                else:
                    pre.next = start.next
                    start = pre.next
            else:
                pre = start
                start = start.next
        return head