# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        absolute = 99999999
        temp = []
        def tree(root):
            if not root:
                return
            if root.left:
                tree(root.left)
            temp.append(root.val)
            if root.right:
                tree(root.right)
                
                
        tree(root)
        n=len(temp)
        #print(temp)
        for i in range(n-1):
            val = abs(temp[i]-temp[i+1])
            if absolute>val:
                absolute = val
        return absolute