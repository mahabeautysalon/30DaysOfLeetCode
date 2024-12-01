import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def sets(nums,arr):
            if(not nums):
                if arr not in self.ans:
                    self.ans.append(copy.deepcopy(arr))
                return
            for i in range(len(nums)):
                sets(nums[i+1:],arr)
                arr.append(nums[i])
                sets(nums[i+1:],arr)
                #print(f"before pop : {arr}")
                arr.pop()
                #print(f"afer pop : {arr}")
        sets(nums,[])
        return self.ans