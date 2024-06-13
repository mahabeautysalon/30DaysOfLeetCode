class Solution:
    def minimumChairs(self, s: str) -> int:
        count,maxCount=0,0
        for i in s:
            if(i=='E'):
                count+=1
            else:
                count-=1
            if(maxCount<count):
                maxCount=count
        #print(s[0])
        return maxCount
        