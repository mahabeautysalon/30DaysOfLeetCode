class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumVal = sum(nums[:k])
        maxAverage = sumVal/k
        n = len(nums)
        if n == 1:
            return nums[0]/1
        for i in range(1,n-k+1):
            sumVal= sumVal-nums[i-1]+nums[i+k-1]
            average = (sumVal/k)
            if maxAverage < average:
                maxAverage = average
        return maxAverage