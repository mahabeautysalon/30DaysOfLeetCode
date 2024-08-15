# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        ans = [root.val]
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    temp.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    temp.append(node.right.val)
                    queue.append(node.right)
            if len(temp)>0:
                ans = temp
        return ans[0]