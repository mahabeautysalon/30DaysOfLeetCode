class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinctNum1 =[]
        distinctNum2 =[]
        if len(nums1) < len(nums2):
            n=len(nums2)
        else:
            n = len(nums1)
        for i in range(n):
            if i<len(nums1) and nums1[i] not in nums2 and nums1[i] not in distinctNum1:
                distinctNum1.append(nums1[i])
            if i<len(nums2) and nums2[i] not in nums1 and nums2[i] not in distinctNum2:
                distinctNum2.append(nums2[i])
        ans = []
        ans.append(distinctNum1)
        ans.append(distinctNum2)
        return ans