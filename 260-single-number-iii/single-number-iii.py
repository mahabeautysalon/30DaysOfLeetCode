class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for val in nums:
            if nums.count(val)==1:
                res.append(val)
        return res