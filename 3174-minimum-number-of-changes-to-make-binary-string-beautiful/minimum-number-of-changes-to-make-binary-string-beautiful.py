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
            substrings = re.findall('.{1,2}', s)
            for val in substrings:
                if(len(set(val)) == 2):
                    result += 1
        return result