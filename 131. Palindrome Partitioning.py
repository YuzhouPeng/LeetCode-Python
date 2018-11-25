def isPalindrome(s,begin,end):
    while begin<end:
        if s[begin]!=s[end]:
            return False
        begin+=1
        end-=1
    return True
def doPartition(s,partitions,temppartition):
    if len(s)==0:
        partitions.append(list(temppartition))
        return
    for i in range(len(s)):
        if isPalindrome(s,0,i):
            temppartition.append(s[:i+1])
            doPartition(s[i+1:],partitions,temppartition)
            del temppartition[len(temppartition)-1]


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partitions = []
        temppartitions = []
        doPartition(s,partitions,temppartitions)
        return partitions