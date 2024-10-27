class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            beg, end = 0, len(matrix[0])
            mid = (beg+end)//2
            while(beg < end and matrix[i][mid] != target):
                if(matrix[i][mid] < target):
                    beg = mid+1
                else:
                    end = mid-1
                mid = (beg + end)//2
                
            
            if mid >= 0 and mid < len(matrix[0]) and matrix[i][mid] == target:
                return True
        return False
