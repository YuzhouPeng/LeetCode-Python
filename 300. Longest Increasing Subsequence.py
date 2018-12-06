def binarysearch(tails,length,key):
    l=0
    h = length
    while l<h:
        mid = l+int((h-l)/2)
        if tails[mid]==key:
            return mid
        elif tails[mid]>key:
            h = mid
        else:
            l = mid+1


    return l
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tails = [0]*n
        length = 0
        for num in nums:
            index = binarysearch(tails,length,num)
            tails[index] = num
            if index==length:
                length+=1

        return length