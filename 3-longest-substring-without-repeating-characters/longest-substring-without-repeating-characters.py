class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_count = 0
        first = 0
        last = 1
        if(n==1):
            return 1
        
        while(first <= last and last<=n):
            size = len(s[first:last])
            if(size == len(set(s[first:last]))):
                if(max_count < size):
                    max_count = size
                last+=1
            else:
                first+=1
                
        return max_count
