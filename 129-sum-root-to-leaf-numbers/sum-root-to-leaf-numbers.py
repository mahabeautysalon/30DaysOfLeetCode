# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def findPaths(root,path,paths):
            if not root:
                return
            path.append(str(root.val))
            if root.left==None and root.right==None:
                paths.append("".join(path))
            else:
                findPaths(root.left,path,paths)
                findPaths(root.right,path,paths)
            path.pop()
        paths = []
        sumVal = 0
        findPaths(root,[],paths)
        for val in paths:
            sumVal += int(val)
        return sumVal