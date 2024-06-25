# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bst(self,root,value):
    if not root:
        return 
    bst(self,root.right,value)
    value.val += root.val
    root.val = value.val
    bst(self,root.left,value)
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        value = TreeNode(0)
        bst(self,root,value)
        return root