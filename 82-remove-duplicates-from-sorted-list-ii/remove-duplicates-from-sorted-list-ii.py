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
        pre = start
        while start!=None and start.next != None:
            if start.val == start.next.val:
                temp = start.next
                while temp and start.val == temp.val:
                    #print(f"start value : {start.val} and temp value : {temp.val}")
                    temp = temp.next
                if start == head:
                    head = temp
                else:
                    pre.next = temp
                    start = pre.next
            else:
                pre = start
                start = start.next
        return head
        