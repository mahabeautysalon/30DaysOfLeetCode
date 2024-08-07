# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sumVal = 0
        def findPaths(root,path,paths):
            if not root:
                return
            path+=str(root.val)
            if root.left==None and root.right==None:
                paths.append(int(path))
                self.sumVal += int(path)
            else:
                findPaths(root.left,path,paths)
                findPaths(root.right,path,paths)
            #print(path)
            #print(paths)
            path = path[:-1]
        paths = []
        findPaths(root,"",paths)
        return self.sumVal