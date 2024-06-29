class Solution:
    def removeStars(self, s: str) -> str:
        while s.find("*")!=-1:
            ind = s.find("*")
            s = s[:ind-1]+s[ind+1:]
        return s
        