class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, sufix = [1]*n, [1]*n
        ans = [0]*n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            sufix[i] = sufix[i+1]*nums[i+1]
        #print(prefix)
        #print(sufix)
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]
        for i in range(n):
            ans[i] = prefix[i]*sufix[i]
        return ans