class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while(pow(2,i)<n):
            i+=1
        if n == pow(2,i):
            return True
        else:
            return False