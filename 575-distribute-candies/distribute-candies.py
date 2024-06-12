class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        print(unique_candies)
        min_candies = len(candyType)//2
        return min(min_candies,len(unique_candies))
        