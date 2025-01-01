class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        tel = {
            '2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl",
            '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"
        }
        self.result = []
        # ["abc","def"]
        def combination(i,cur):
            if(len(digits) == len(cur)):
                self.result.append("".join(cur))
                return
            for val in tel[digits[i]]:
                cur.append(val)
                combination(i+1,cur)
                cur.pop()
        combination(0,[])
        return self.result