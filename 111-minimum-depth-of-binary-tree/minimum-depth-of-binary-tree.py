# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.minDep = 100000
        def tree(root,path):
            if not root:
                return
            path.append(root.val)
            if root.left == None and root.right == None:
                length = len(path)
                if self.minDep > length:
                    self.minDep = length
            tree(root.left,path)
            tree(root.right,path)
            path.pop()
        tree(root,[])
        return self.minDep