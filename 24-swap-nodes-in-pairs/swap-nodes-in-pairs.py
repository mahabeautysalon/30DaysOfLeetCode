# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        start = head
        head = start.next
        start.next = start.next.next
        head.next = start
        start = head.next
        while start.next!=None:
            temp = start.next
            start.next = start.next.next
            if start.next is not None:
                temp.next = start.next.next
                start.next.next = temp
                start = start.next.next
            else:
                temp.next = None
                start.next = temp
                start = start.next
        return head

        