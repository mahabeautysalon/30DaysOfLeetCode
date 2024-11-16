class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans = []
        res = 0
        for i in range(n-k+1):
            temp = nums[i:(i+k)]
            res = temp[-1]
            for j in range(k-1):
                if (temp[j]+1) != temp[j+1]:
                    res = -1
                    break
            ans.append(res)
        return ans