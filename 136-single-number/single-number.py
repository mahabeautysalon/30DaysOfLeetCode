class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        for val in nums:
            if temp.get(val):
                temp[val] +=1
            else:
                temp[val] = 1  
        sorted_id = sorted(temp.items(), key=lambda x:x[1])
        return sorted_id[0][0]
        