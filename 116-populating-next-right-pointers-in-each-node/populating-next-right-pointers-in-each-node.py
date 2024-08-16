"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = collections.deque([root])
        root.next = None
        temp = queue
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
            temp = queue.copy()
            if temp:
                pre = temp.popleft()
            for j in range(len(temp)):
                curr = temp.popleft()
                if pre:
                    pre.next = curr
                    pre = curr
        return root
