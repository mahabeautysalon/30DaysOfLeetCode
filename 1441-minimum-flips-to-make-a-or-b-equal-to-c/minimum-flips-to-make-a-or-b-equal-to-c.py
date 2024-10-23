
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while(c > 0 or a > 0 or b > 0):
            if(1 & c):
                if(not ( (1 & a) | (1 & b) ) ):
                    count += 1
            else:
                if(1 & a):
                    count += 1
                if(1 & b):
                    count += 1
            c = c >> 1
            a = a >> 1
            b = b >> 1
        return count