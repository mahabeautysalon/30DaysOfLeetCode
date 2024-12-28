class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if(len(set(nums)) == n):
            return 0
        ans = 0
        ind = 0
        while(len(set(nums[ind:])) != len(nums[ind:])):
            ans += 1
            ind+=3
        return ans