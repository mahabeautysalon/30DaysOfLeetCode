class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        count= 1
        maxFrequency= -1
        pre = 0
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
            else:
                if count == arr[i]:
                    if maxFrequency < arr[i]:
                        maxFrequency = arr[i]
                count = 1
        if count == arr[-1]:
            if maxFrequency < arr[i]:
                maxFrequency = arr[i]
        return maxFrequency