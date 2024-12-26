from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans, i = 0, 0
        while(tickets[k] > 0):
            if tickets[i] > 0:
                tickets[i] -= 1
                ans += 1
            i = (i+1) % n
        return ans