from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        data = permutations(nums)
        return data