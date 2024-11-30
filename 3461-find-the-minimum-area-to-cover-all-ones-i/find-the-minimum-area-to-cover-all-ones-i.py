class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minArea, sRow, eRow, sCol, eCol = 0,len(grid),len(grid),len(grid),0
        #ind = []
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == 1 and i < sCol:
                    sCol = i
                if(grid[j][i] == 1 and eCol < i):
                    eCol = i
            if 1 in grid[j] and j < sRow:
                sRow = j
            if 1 in grid[j]:
                eRow = j
            #print(f"rows and col value : {sRow} : {eRow} : {sCol} : {eCol}")
        rows, col = eRow - sRow+1, eCol - sCol+1
        
        #print(f"rows and col value : {sRow} : {eRow} : {sCol} : {eCol}")
        minArea = rows*col
        return minArea