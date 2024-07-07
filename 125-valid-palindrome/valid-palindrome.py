class Solution(object):
    def isPalindrome(self, s):
        temp = s.lower()
        temp = ''.join(c for c in temp if c.isalnum())
        if temp == temp[::-1]:
            return True
        return False