class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = []
        for val in nums1:
            if val in nums2:
                ans.append(val)
        return ans