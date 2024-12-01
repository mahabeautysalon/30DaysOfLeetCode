from bisect import bisect_left
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alpha = [
                    "a","b","c","d","e","f","g",
                    "h","i","j","k","l","m","n","o",
                    "p","q","r","s","t","u","v","w",
                    "x","y","z"
                ]
        temp = str()
        val, quotient, module = 26, 1, 1
        while(n>0):
            if(k-(n-1)<= 26):
                return alpha[0]*(n-1) + alpha[k-n] + temp
            else:
                quotient = k // val
                module = k % val
                n -= quotient
                if(module < n):
                    while(n>module):
                        n += 1
                        quotient -= 1
                        module += 26
                temp = alpha[val-1]*quotient + temp
                k = module
        return temp
