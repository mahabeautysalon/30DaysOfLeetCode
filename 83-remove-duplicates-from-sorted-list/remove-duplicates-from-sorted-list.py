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
                temp = start.next
                while temp and start.val == temp.val:
                    temp = temp.next
                start.next = temp
            else:
                start = start.next
        return head