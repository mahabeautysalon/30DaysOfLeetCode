# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        que = collections.deque([root])

        while(que):
            temp = []
            for i in range(len(que)):
                node = que.popleft()
                temp.append(node.val)
                if(node.left):
                    que.append(node.left)
                if(node.right):
                    que.append(node.right)
            ans.insert(0, temp)
        return ans
