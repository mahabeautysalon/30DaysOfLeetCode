class Solution:
    def reverse(self, x: int) -> int:
        result=0
        check=False
        if x < 0:
            check = True
            x = x * (-1)
        while x > 0:
            q = x%10
            x = x // 10
            result = (result * 10 )+q
        if check:
            result = result * (-1)
            if result < -2147483648:
                return 0
        else:
            if result > 2147483647:
                return 0
        return result
        