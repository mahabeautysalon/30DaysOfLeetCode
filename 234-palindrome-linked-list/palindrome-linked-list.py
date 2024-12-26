# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        node = head
        while(node != None):
            stack.append(node.val)
            node = node.next
            
        if(stack == stack[::-1]):
            return True
        return False