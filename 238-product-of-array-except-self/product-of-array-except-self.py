class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, sufix = [1]*n, [1]*n
        ans = [0]*n
        right = n-2
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            sufix[right] = sufix[right+1]*nums[right+1]
            right -= 1
        for i in range(n):
            ans[i] = prefix[i]*sufix[i]
        return ans