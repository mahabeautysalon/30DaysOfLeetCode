class Solution:
    def myPow(self, x: float, n: int) -> float:
        check = False
        if n < 0 :
            check = True
            n *= -1
        res = 1
        while(n>0):
            if (n & 1):
                res *= x
            n = n >> 1
            x *= x
        if check:
            res = (1/res)
        return res