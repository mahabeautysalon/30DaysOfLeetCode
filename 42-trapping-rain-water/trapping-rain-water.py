class Solution:
    def trap(self, height: List[int]) -> int:
        n, s_len = len(height), 1
        r = [0]*n
        l = [0]*n
        stack = [height[0]]
        # [0]
        for i in range(n):
            while(s_len > 0 and stack[s_len-1] <= height[i]):
                stack.pop()
                s_len -= 1
                
            if(s_len == 0):
                l[i] = -1
                stack.append(height[i])
                s_len += 1
            else:
                l[i] = stack[s_len-1]
                if(s_len > 0 and stack[s_len-1] < height[i]):
                    stack.append(height[i])
                    s_len += 1
            
            #print(l)
        stack = [height[n-1]]
        s_len = 1
        for i in range(n-1,-1,-1):
            while(s_len > 0 and stack[s_len-1] <= height[i]):
                stack.pop()
                s_len -= 1
                
            if(s_len == 0):
                r[i] = -1
                stack.append(height[i])
                s_len += 1
            else:
                r[i] = stack[s_len-1]
                if(s_len > 0 and stack[s_len-1] < height[i]):
                    stack.append(height[i])
                    s_len += 1
            #print(r)
            #print(stack)
        ans, minVal = 0, 0
        for i in range(n):
            if(r[i] != -1 and l[i] != -1):
                minVal = min(r[i],l[i])
                ans += (minVal - height[i])
            #print(f"ans : {ans} minValue : {minVal} height : {height[i]} ", end=" ")
            #print(f"r[i] : {r[i]} l[i] : {l[i]}")
        return ans
                