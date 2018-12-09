class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        l = len(num)
        if l % 2 == 0:
            z = (num[int((l / 2) - 1)] + num[int(l / 2)]) / 2
        else:
            z = num[int((l - 1) / 2)]

        return z