class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        beg,end=0,int(math.sqrt(c))
        while beg<=end:
            if (beg*beg) + (end*end) == c:
                return True
            elif (beg*beg) + (end*end) > c:
                end-=1
            else:
                beg+=1
            #print(f"beg : {beg}")
            #print(f"end : {end}")
            #print(f"res : {(beg*beg)+(end*end)}")
        return False