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
        temp = [root.val]
        def tree(root):
            if not root:
                return
            if root.left:
                temp.append(root.left.val)
                tree(root.left)
            if root.right:
                temp.append(root.right.val)
                tree(root.right)
        tree(root)
        n=len(temp)
        #print(temp)
        for i in range(n):
            for j in range(i+1, n):
                val = abs(temp[i]-temp[j])
                if absolute>val:
                    absolute = val
        return absolute