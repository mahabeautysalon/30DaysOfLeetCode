class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n, r = (m+n-2), n-1
        return (math.factorial(n)//(math.factorial(r)*math.factorial(n-r)))