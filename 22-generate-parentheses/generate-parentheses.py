class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, ans = [], []
        def genParenthesis(open, close):
            if open == close == n:
                ans.append("".join(stack))

            if(open < n):
                stack.append("(")
                genParenthesis(open+1, close)
                stack.pop()
            if(close < open):
                stack.append(")")
                genParenthesis(open, close+1)
                stack.pop()

        genParenthesis(0,0)
        return ans
