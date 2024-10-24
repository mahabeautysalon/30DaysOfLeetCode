import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and root2:
            return False
        elif not root1 and not root2:
            return True
        elif root1 and root2 and root1.val != root2.val:
            return False

        def levelTraversal(q):
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    #print("level traversal func ",end=" ")
                    #print(node.val)
                    if node.left:
                        q.append(node.left)
                        temp.append(node.left.val)
                    else:
                        temp.append(0)
                    if node.right:
                        q.append(node.right)
                        temp.append(node.right.val)
                    else:
                        temp.append(0)
            return temp,q
        def minVal(a,b):
            if a < b:
                return a
            else:
                return b
        
        q1 = collections.deque([root1])
        q2 = collections.deque([root2])
        while(q1 and q2):
            temp_q1 = copy.copy(q1)
            temp_q2 = copy.copy(q2)
            temp1,q11 = levelTraversal(q1)
            temp2,q22 = levelTraversal(q2)
            #print("Frist check ")
            #print(temp1)
            #print(temp2)
            q1 = q11
            q2 = q22
            if(temp1 != temp2):
                q1 = copy.copy(temp_q1)
                q2 = copy.copy(temp_q2)
                n1 = len(q1)
                n2 = len(q2)
                n= minVal(n1,n2)
                
                for i in range(n):
                    #print("inside the for loop",end=" ")
                    node1 = q1.popleft()
                    node2 = q2.popleft()
                    #print(node1.val)
                    if node1 and node2:
                        if (node1.left and node2.right):
                            if (node1.left.val == node2.right.val):
                                node1.left, node1.right = node1.right, node1.left
                        elif (node2.left and node1.right):
                            if (node1.right.val == node2.left.val):
                                node1.left, node1.right = node1.right, node1.left
                temp1,q1 = levelTraversal(temp_q1)
                temp2,q2 = levelTraversal(temp_q2)
                #print(" ")
                #print("second check")
                #print(temp1)
                #print(temp2)
                if(temp1 != temp2):
                    return False
            
        if len(q1)>0 or len(q2):
            #print("one of queue is not empty")
            return False
        return True
        