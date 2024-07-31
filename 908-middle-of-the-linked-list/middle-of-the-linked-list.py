# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next !=None:
            #print(f"slow : {slow.val}")
            #print(f"fast : {fast.val}")
            slow = slow.next
            if fast.next !=None:
                fast = fast.next.next
            else:
                fast = fast.next
        return slow
                