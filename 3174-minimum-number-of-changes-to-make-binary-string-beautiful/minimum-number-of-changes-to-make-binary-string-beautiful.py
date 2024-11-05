class Solution:
    def minChanges(self, s: str) -> int:
        if(len(s)== 2):
            if(s[0] != s[1]):
                return 1
            else:
                return 0
        elif(len(set(s))==1):
            return 0
        else:
            result = 0
            substrings = [s[i:i+2] for i in range(0, len(s), 2) if(len(set(s[i:i+2])) == 2)]
        return len(substrings)