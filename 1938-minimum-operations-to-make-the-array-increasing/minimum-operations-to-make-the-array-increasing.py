class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOper=0
        for i in range(len(nums)-1):
            if(nums[i]>=nums[i+1]):
                minOper += (nums[i]-nums[i+1]+1)
                nums[i+1] = nums[i]+1
        return minOper

        