# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        start = head
        while start:
            binary.append(str(start.val))
            start = start.next
        temp = "".join(binary)
        return int(temp,2)