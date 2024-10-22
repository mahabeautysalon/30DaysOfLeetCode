# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        que = collections.deque([root])
        check = False
        while(que):
            temp = []
            for i in range(len(que)):
                node = que.popleft()
                temp.append(node.val)
                if(node.left):
                    que.append(node.left)
                if(node.right):
                    que.append(node.right)
                
            
            if(check):
                check = False
                temp = temp[::-1]
            else:
                check = True
            ans.append(temp)
        return ans
