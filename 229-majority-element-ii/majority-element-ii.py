class Solution(object):
    def majorityElement(self, nums):
        unique = set(nums)
        n=len(nums)
        appear = n//3
        res = []
        for val in unique:
            if nums.count(val)>appear:
                res.append(val)
        return res