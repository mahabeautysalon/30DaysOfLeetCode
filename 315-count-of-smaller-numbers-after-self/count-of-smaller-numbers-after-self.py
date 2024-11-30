from bisect import bisect_left
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        temp = SortedList(nums)
        for i in range(len(nums)-1):
            temp.remove(nums[i])
            if(len(temp) < 2):
                if(len(temp) > 0 and temp[0] < nums[i]):
                    ans.append(1)
                    continue
                else:
                    ans.append(0)
                    continue
            elif(temp[-1] < nums[i]):
                ans.append(len(temp))
                continue
            pos = bisect_left(temp,nums[i])
            ans.append(pos)
        ans.append(0)
        return ans