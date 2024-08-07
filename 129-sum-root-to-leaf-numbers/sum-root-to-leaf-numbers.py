# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sumVal = 0
        def findPaths(root,path):
            if not root:
                return
            path+=str(root.val)
            if root.left==None and root.right==None:
                self.sumVal += int(path)
            else:
                findPaths(root.left,path)
                findPaths(root.right,path)
            #print(path)
            #print(paths)
            path = path[:-1]
        findPaths(root,"")
        return self.sumVal