# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        start = head
        temp = None
        tail=None
        while start.next!=None:
            if temp==None:
                temp = start.next
                start.next= start.next.next
                temp.next=None
                tail=temp
            else:
                tail.next = start.next
                start.next= start.next.next
                tail=tail.next
                tail.next = None
            if start.next!=None:
                start = start.next
        start.next=temp
        return head
