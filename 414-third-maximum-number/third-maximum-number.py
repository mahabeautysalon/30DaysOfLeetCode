class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = list(set(nums))
        maxValue1,maxValue2,maxValue3=-2147483648,-2147483648,-2147483648
        for i in range(2):
            for val in temp[::-1]:
                if (val > maxValue1):
                    maxValue1 = val
                if(val > maxValue2 and maxValue1 > maxValue2 and maxValue1 != val):
                    maxValue2 = val
                if(val > maxValue3 and maxValue3 < maxValue2 and maxValue3 < maxValue1 and maxValue1 != val and maxValue2 != val):
                    maxValue3 = val
        if(len(temp)>2):
            return maxValue3
        return maxValue1
        