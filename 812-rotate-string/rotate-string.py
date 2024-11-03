class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = s[-1] + s[:-1]
        if temp == goal:
            return True
        #print(temp)
        while(s!=temp):
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False
