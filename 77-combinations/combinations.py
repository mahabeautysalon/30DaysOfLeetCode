from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        val = range(1,n+1)
        com = combinations(val,k)
        ans = []
        for c in com:
            ans.append(list(c))
        return ans