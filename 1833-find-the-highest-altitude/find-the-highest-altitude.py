class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest=0
        for val in gain:
            altitude+=val
            if highest<altitude:
                highest=altitude
        return highest
