class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [val for val in nums if val>0]
        neg = [val for val in nums if val<0]
        ans = []
        n=len(neg)
        for i in range(n):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans