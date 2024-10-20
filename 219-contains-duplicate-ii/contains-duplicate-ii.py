class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        for i in range(n-1):
            #print(nums[i:i+k+1])
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False