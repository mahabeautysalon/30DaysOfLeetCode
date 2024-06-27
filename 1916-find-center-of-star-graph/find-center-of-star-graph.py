class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = 0
        row1 = edges[0]
        row2 = edges[1]
        for val in row1:
            for val2 in row2:
                if val == val2:
                    return val
                    