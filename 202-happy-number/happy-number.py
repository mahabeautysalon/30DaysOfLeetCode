class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        digits = list(n)
        happy = "".join(digits)
        count = 0
        while(happy != "1" and count < 20):
            temp = 0
            for val in digits:
                temp += int(val)**2
            #print(temp)
            temp = str(temp)
            digits = list(temp)
            happy = "".join(digits)
            count+=1
        if happy == "1":
            return True
        return False