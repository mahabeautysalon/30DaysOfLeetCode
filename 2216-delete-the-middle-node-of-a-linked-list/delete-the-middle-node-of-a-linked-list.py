# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        elif head.next == None:
            head = head.next
            return head
        fast = head
        slow=head
        pre = slow
        while fast and fast.next != None:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = pre.next.next
        return head