class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_no, L_no = 0, 0
        maxCount = 0
        for i in range(len(s)):
            if(s[i] == 'R'):
                r_no += 1
            else:
                L_no += 1
            if(r_no == L_no):
                maxCount += 1
                r_no = 0
                L_no = 0
        return maxCount
