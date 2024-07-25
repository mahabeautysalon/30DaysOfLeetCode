"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        queue = collections.deque([node])
        duplicates = {node.val: Node(node.val, [])}
        while queue:
            orignal_node = queue.popleft()
            duplicate_node = duplicates[orignal_node.val]
            for neighbor in orignal_node.neighbors:
                if neighbor.val not in duplicates:
                    duplicates[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                duplicate_node.neighbors.append(duplicates[neighbor.val])
        return duplicates[node.val]
