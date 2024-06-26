class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        result = []
        n = len(num)
        for i,_ in enumerate(num):
            while result and result[-1] > num[i] and k > 0:
                result.pop()
                k -=1
            result.append(num[i])
        result = result[:len(result)-k]
        return "".join(result).lstrip("0") or "0"

