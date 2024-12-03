class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        last = len(spaces)-2
        beg = 0
        left = s[:spaces[0]] + " "
        right = " "  + s[spaces[last+1]:len(s)]
        while(beg<last):
            left += s[spaces[beg]:spaces[beg+1]] + " "
            right = " " + s[spaces[last]:spaces[last+1]] + right
            beg += 1
            last -= 1
        if(len(spaces)%2 == 0):
            left += s[spaces[beg]:spaces[beg+1]] + " "
        return left[:-1]+right