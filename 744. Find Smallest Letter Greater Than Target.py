class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        length1 = len(letters)
        l=0
        r = length1-1
        while(l<=r):
            mid = l+(r-l)/2
            if letters[mid]<=target:
                l = mid+1
            else:
                r = mid-1

        if l<length1:
            return letters[l]
        else:
            return letters[0]
