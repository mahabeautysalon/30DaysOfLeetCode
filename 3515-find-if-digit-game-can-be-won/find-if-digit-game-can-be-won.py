class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleDigit = 0
        doubleDigit = 0
        for val in nums:
            if val>9:
                doubleDigit +=val
            else:
                singleDigit += val
        if doubleDigit == singleDigit:
            return False
        return True