class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        minIncrement = 0
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]>=nums[i+1]):
                minIncrement += (nums[i]-nums[i+1]+1)
                nums[i+1] = nums[i]+1
        return minIncrement
