class Solution(object):

    def find_the_median_k(self, alist, blist,k):
        lengtha = len(alist)
        lengthb = len(blist)
        if lengtha > lengthb:
            return self.find_the_median_k(blist, alist, k)
        if lengtha ==0:
            return blist[k-1]
        if k ==1:
            return min(alist[0],blist[0])
        parameter_a = min(k/2, lengtha)
        parameter_b = k-parameter_a

        if alist[parameter_a-1]<=blist[parameter_b-1]:
            return self.find_the_median_k(alist[parameter_a:],blist,parameter_b)
        else:
            return self.find_the_median_k(alist,blist[parameter_b:],parameter_a)


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length_alist = len(nums1)
        length_blist = len(nums2)
        if ((length_alist+length_blist)%2==1):
            return self.find_the_median_k(nums1,nums2,(length_alist+length_blist)/2+1)
        else:
            return (self.find_the_median_k(nums1,nums2,(length_alist+length_blist)/2)+self.find_the_median_k(nums1,nums2,(length_alist+length_blist)/2+1))*0.5