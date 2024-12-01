class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minSum, curSum = (2)**31, 0
        n = len(nums)
        for j in range(l,r+1):
            for i in range(n-j+1):
                curSum = sum(nums[i:i+j])
                if curSum > 0:
                    minSum = min(minSum, curSum)
                
        if(minSum == (2)**31):
            return -1
        return minSum