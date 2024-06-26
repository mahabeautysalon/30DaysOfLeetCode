class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for val in arr:
            if count.get(val):
                count[val] +=1
            else:
                count[val] = 1
        print(count)
        maxFrequency = -1
        for key,val in count.items():
            if key==val and maxFrequency < val:
                maxFrequency = val
        return maxFrequency