class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        maxlength = (length*(length+1))//2
        sumval = sum(nums)
        #print(sumval)
        #print(maxlength)
        return (maxlength-sumval)