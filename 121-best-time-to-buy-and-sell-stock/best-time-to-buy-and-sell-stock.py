class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = [0]*len(prices)
        temp[-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            temp[i] = max(prices[i],temp[i+1])
        maxProfit = (-2)**31
        for i in range(len(prices)):
            maxProfit = max(maxProfit, (temp[i] - prices[i]))
        return maxProfit