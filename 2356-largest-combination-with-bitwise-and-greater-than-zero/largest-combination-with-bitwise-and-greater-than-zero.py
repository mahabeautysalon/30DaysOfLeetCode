from itertools import combinations 
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maximum = -1
        maxCount = 0
        for i in range(24):
            count = 0

            for can in candidates:
                if(can & (1 << i)):
                    count += 1
            maxCount = max(maxCount, count)

        return maxCount