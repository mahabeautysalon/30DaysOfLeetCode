class Solution:
    def getLucky(self, s: str, k: int) -> int:
        val = "abcdefghijklmnopqrstuvwxyz"
        resultingInt = []
        for ch in s:
            resultingInt.append(str(val.find(ch)+1))
        temp = "".join(resultingInt)
        for i in range(k):
            int_list = [int(char) for char in temp]
            temp = str(sum(int_list))
        return int(temp)