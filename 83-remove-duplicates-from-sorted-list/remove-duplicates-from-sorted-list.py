# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return head
        start = head
        while start!=None and start.next!=None:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next
        return head