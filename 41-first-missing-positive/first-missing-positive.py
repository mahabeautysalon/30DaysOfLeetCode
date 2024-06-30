class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i,n=1,len(nums)
        nums.sort()
        start,end = 0,n-1
        mid = (start+end)//2
        for j in range(n):
            start,end = 0,n-1
            mid = (start+end)//2
            while(start<=end and nums[mid]!=i):
                if (nums[mid]<i):
                    start = mid+1
                else:
                    end = mid-1
                mid = (start+end)//2
            if nums[mid]!=i:
                return i
            else:
                i+=1
        return i