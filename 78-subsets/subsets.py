import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def sets(nums,arr):
            print(arr)
            if(not nums):
                if arr not in self.ans:
                    self.ans.append(copy.deepcopy(arr))
                return
            for i in range(len(nums)):
                sets(nums[i+1:],copy.deepcopy(arr))
                arr.append(nums[i])
                sets(nums[i+1:],copy.deepcopy(arr))
        
        sets(nums,[])
        return self.ans