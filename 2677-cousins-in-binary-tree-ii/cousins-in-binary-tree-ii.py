# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.val = 0
        if root.left:
            root.left.val = 0
        if root.right:
            root.right.val = 0
        q = collections.deque([root.left,root.right])
        temp = collections.deque([])
        levelSum = 0
        if root.left:
            if root.left.left:
                levelSum += root.left.left.val
            if root.left.right:
                levelSum += root.left.right.val
        if root.right:
            if root.right.left:
                levelSum += root.right.left.val
            if root.right.right:
                levelSum += root.right.right.val
            
        while(q):
            totalSum = levelSum
            """print(f"total sum : {totalSum}")
            print(" ")"""
            levelSum = 0
            
            childSum = 0
            for i in range(len(q)):
                node = q.popleft()
                #levelSum += node.val

                if node:
                    if node.left:
                        childSum += node.left.val
                        q.append(node.left)
                        if node.left.left:
                            levelSum += node.left.left.val
                        if node.left.right:
                            levelSum += node.left.right.val

                    if node.right:
                        childSum += node.right.val
                        q.append(node.right)
                        if node.right.left:
                            levelSum += node.right.left.val
                        if node.right.right:
                            levelSum += node.right.right.val

                    """print(f"total sum : {totalSum}")
                    print(f"level sum : {levelSum}")
                    print(f"child sum : {childSum}")
                    print(" ")"""

                    # setting sum values     
                    sumVal = totalSum - childSum
                    if node.left:
                        node.left.val = sumVal
                    if node.right:
                        node.right.val = sumVal
                    childSum = 0

                
            """print(" ")
            print(f"total sum : {totalSum}")
            print(f"level sum : {levelSum}")
            print(f"child sum : {childSum}")
            print(" ")"""

        return root
            