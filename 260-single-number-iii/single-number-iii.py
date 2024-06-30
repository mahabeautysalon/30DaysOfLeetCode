class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for val in nums:
            if val not in res:
                res.append(val)
            else:
                res.remove(val)
            #print(res)
        return res