class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return False
        Flag = False
        i = 1
        count=0
        while i<len(A):
            if i+1<len(A) and A[i-1]<A[i] and A[i]>A[i+1]:
                Flag=True
                count+=1
            elif A[i-1]>=A[i] and Flag==False:
                return False
            elif Flag==True and A[i-1]<=A[i]:
                return False
            i+=1
        if i==len(A) and Flag==False:
            return False
        if count>1:
            return False
        return True