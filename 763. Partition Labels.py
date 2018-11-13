def chartoindex(c):
    return ord(c)-ord('a')
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lastindexofchar = [None for i in range(26)]
        for i in range(len(S)):
            lastindexofchar[chartoindex(S[i])] = i
        partitions = []
        firstindex = 0
        while firstindex<len(S):
            lastindex = firstindex
            for i in range(firstindex,len(S)):
                if i<=lastindex:
                    index = lastindexofchar[chartoindex(S[i])]
                    if index>lastindex:
                        lastindex = index
            partitions.append(lastindex-firstindex+1)
            firstindex = lastindex+1
        return partitions
