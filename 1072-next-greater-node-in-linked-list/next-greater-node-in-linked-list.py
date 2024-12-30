# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        def recurse(head):
            if not head.next:
                ans.append(0)
                stack.append(head.val)
                return 
            val = recurse(head.next)
            while(len(stack) > 0 and stack[-1] <= head.val):
                stack.pop()
            if(len(stack) > 0):
                ans.append(stack[-1])
            else:
                ans.append(0)
            stack.append(head.val)
        recurse(head)
        return ans[::-1]
            