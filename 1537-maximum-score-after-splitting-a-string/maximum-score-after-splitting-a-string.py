class Solution:
    def maxScore(self, s: str) -> int:
        left, right, ones = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
        right = ones
        score = 0
        for i in range(len(s)-1):
            if(s[i] == '0'):
                left += 1
            else:
                right -= 1
            score = max(score, (left+right))
        return score