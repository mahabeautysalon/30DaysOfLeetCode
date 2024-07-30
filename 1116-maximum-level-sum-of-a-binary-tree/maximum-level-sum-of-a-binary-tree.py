# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        maxSum=root.val
        level = 1
        maxLevel = 1
        while queue:
            n=len(queue)
            sumVal=0
            level+=1
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    sumVal += node.left.val
                if node.right:
                    queue.append(node.right)
                    sumVal += node.right.val
            #print(f"Level : {level}")
            if sumVal>maxSum:
                maxSum = sumVal
                maxLevel = level
        if maxLevel == level:
            maxLevel-=1
        return maxLevel