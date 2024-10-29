class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        def power(n,exp):
            if n < 4*exp:
                return False
            elif n == 4*exp:
                return True
            else:
                exp = exp*4
                return power(n,exp)
        return power(n,1)