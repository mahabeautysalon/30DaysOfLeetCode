# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def treeTraversal(root,ans):
    if root==None:
        return
    treeTraversal(root.left,ans)
    treeTraversal(root.right,ans)
    ans.append(root.val)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        treeTraversal(root,ans)
        print(ans)
        return ans