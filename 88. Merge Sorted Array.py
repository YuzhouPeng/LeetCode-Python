class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1 = m-1
        index2 = n-1
        indexmerge = m+n-1
        while index1>=0 or index2>=0:
            if index1<0:
                nums1[indexmerge] = nums2[index2]
                indexmerge = indexmerge-1
                index2 = index2-1
            elif index2<0:
                nums1[indexmerge] = nums1[index1]
                indexmerge = indexmerge-1
                index1 = index1-1
            elif nums2[index2]>nums1[index1]:
                nums1[indexmerge] = nums2[index2]
                indexmerge = indexmerge-1
                index2 = index2-1
            else:
                nums1[indexmerge] = nums1[index1]
                indexmerge = indexmerge-1
                index1 = index1-1

