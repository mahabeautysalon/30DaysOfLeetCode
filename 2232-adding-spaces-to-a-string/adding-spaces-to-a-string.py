class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)
        res = s[:spaces[0]] + " "
        for i in range(len(spaces)-1):
            res += s[spaces[i]:spaces[i+1]]  + " " 
            #print(res)
        res += s[spaces[n-1]:len(s)]
        #print(res)
        return res