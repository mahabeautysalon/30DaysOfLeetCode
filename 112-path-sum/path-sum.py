# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.sumpath = False
        def tree(root,path):
            if not root:
                return
            path.append(root.val)
            if root.left == None and root.right == None:
                if sum(path) == targetSum:
                    self.sumpath = True
                    return
            tree(root.left,path)
            tree(root.right,path)
            path.pop()
        tree(root,[])
        return self.sumpath