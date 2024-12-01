from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        nums.sort()
        def backTrack(s, path):
            subsets.append(path)
            for i in range(s, n):
                if(i > s) and nums[i] == nums[i-1]:
                    continue
                backTrack(i+1,path+[nums[i]])
        backTrack(0,[])
        return subsets