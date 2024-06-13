class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairSum=0
        for i in range(0,len(nums),2):
            pairSum+=nums[i]
        return pairSum
        