class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = (n//2)
        temp = set(nums)
        for val in temp:
            if nums.count(val) > majority:
                return val