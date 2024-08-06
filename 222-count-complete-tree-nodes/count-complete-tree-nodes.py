# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count=0
        def tree(root):
            if not root:
                return
            self.count+=1
            tree(root.left)
            tree(root.right)
        tree(root)
        return self.count