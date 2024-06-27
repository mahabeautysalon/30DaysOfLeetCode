class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for val in edges[0]:
            for val2 in edges[1]:
                if val == val2:
                    return val
                    