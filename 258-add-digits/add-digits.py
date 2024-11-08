class Solution:
    def addDigits(self, num: int) -> int:
        temp = str(num)
        while(len(temp)>1):
            currentSum = 0
            digitList = list(temp)
            for val in digitList:
                currentSum += int(val)
            temp = str(currentSum)
        return int(temp)