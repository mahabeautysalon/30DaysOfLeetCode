class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 1
        for i in range(len(s)):
            if( len(res) > 1 and res[-1] == s[i] and res[-2] == s[i]):
                continue
            else:
                res.append(s[i])
            #print(res)
        return "".join(res)