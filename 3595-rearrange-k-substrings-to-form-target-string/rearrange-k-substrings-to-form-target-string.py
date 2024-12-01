from itertools import permutations
from sortedcontainers import SortedList
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        splitList = SortedList()
        splitLen = n // k
        if(splitLen == 1):
            return True
        for i in range(0, n-splitLen+1, splitLen):
            splitList.add(s[i:i+splitLen])
        #print(splitList)
        for i in range(0, n-splitLen+1, splitLen):
            val = t[i:i+splitLen]
            if(val not in splitList):
                return False
            splitList.remove(val)
        return True