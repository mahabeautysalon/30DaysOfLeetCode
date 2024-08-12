class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x=0
        temp = 0
        while n > temp:
            temp = 3**x
            #print(temp)
            x+=1
        if n == temp and temp!=0:
            return True
        return False