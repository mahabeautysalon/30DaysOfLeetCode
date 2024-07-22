class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = sorted(zip(heights,names))
        res = list(zip(*zipped))
        res = list(res[1])
        return res[::-1]