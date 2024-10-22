# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sumValues = []
        queue = collections.deque([root])

        while(queue):
            currentSum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                currentSum += node.val
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            sumValues.append(currentSum)
        maxSum = -1
        if(k>len(sumValues)):
            return -1
        sumValues.sort(reverse=True)
        return sumValues[k-1]
        
            
        
            
