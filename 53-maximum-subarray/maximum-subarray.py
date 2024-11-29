class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        curSum, maxSum = 0, (-2)**31
        for i in range(len(nums)):
            if(curSum < 0):
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum