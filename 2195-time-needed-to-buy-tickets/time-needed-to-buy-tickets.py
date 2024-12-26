from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        n = len(tickets)
        ans = 0
        ind = k
        while(q[k] > 0 and len(q) > 0):
            val = q.popleft()
            if(val > 0):
                val -= 1
                ans += 1
            q.append(val)
            k = (k-1)%n
        return ans