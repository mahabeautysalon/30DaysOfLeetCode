# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        ans = [root.val]
        maxVal = -2147483648
        while(queue):
            maxVal = -2147483648
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    if node.left.val>maxVal:
                        maxVal = node.left.val
                    queue.append(node.left)
                if node.right:
                    if node.right.val>maxVal:
                        maxVal = node.right.val
                    queue.append(node.right)
            ans.append(maxVal)
        if ans:
            ans.pop()
        return ans
