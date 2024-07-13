class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        unique = set(arr)
        countVal = {}
        arr.sort()
        counting=1
        n=len(arr)
        for i,_ in enumerate(arr):
            if i!=n-1 and arr[i] == arr[i+1]:
                counting+=1
            else:
                countVal[arr[i]] = counting
                counting=1
        countVal = sorted(countVal.items(),key=lambda x:x[1])
        i=0
        for val in countVal:
            k -= val[1]
            i+=1
            if k<0:
                i-=1
                break
            elif k==0:
                break
        return len(unique)-i