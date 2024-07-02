class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1)<len(nums2):
            for val in nums1:
                if val in nums2:
                    ans.append(val)
                    nums2.remove(val)
        else:
            for val in nums2:
                if val in nums1:
                    ans.append(val)
                    nums1.remove(val)
        return ans