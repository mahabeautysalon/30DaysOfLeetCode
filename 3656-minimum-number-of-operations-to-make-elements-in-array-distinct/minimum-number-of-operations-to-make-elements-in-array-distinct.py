class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if(len(set(nums)) == n):
            return 0
        ans = 0
        while(len(set(nums)) != len(nums)):
            nums = nums[3:]
            ans += 1
        return ans