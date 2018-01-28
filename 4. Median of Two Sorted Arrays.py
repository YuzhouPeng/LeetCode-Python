class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        Len1 = len(nums1)
        Len2 = len(nums2)
        mid1 = nums1[0]
        mid2 = nums2[Len2-1]
        i = j = 0
        if Len1 == 0 and Len2 % 2 ==0:
            return (nums2[Len2/2]+nums2[(Len2/2)-1])/2
        elif Len2 == 0 and Len1 % 2 ==0:
            return (nums1[Len1/2]+nums1[(Len1/2)-1])/2
        elif Len1 == 0 and Len2 % 2 == 1:
            return nums2[Len2/2]
        elif Len2 == 0 and Len1 % 2 == 1:
            return nums1[Len1/2]
        elif Len1 == 0 and Len2 == 0:
            return -1
        def binarysearch(self,numLen1,numLen2):
            if numLen1>Len1:
                

        while i < Len2 and j < Len1:
            if mid1 < mid2:

