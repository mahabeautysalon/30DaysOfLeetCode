# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False
        self.res = []
        def tree(root)->List[int]:
            if not root:
                return

            if not root.left and not root.right:
                self.res.append(root.val)
            #print(temp)

            tree(root.left)
            tree(root.right)
        tree(root1)
        temp1 = self.res
        self.res = []
        temp2 = tree(root2)
        temp2 = self.res
        if temp1 == temp2:
            return True
        return False