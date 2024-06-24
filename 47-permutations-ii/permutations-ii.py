from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #unique = set(nums)
        data = permutations(nums)
        res = []
        for row in data:
            if row not in res:
                res.append(row)
        return res