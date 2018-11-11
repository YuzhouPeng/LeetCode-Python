def compareTo(this, that):
    return ((this > that) - (this < that))
def isValid(s, target):
    i=0
    j=0
    while i<len(s) and j<len(target):
        if s[i] == target[j]:
            j = j+1
        i = i+1
    return j==len(target)

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longeststring = ""
        for target in d:
            l1 = len(longeststring)
            l2 = len(target)
            if l1>l2 or (l1==l2 and compareTo(longeststring, target)<0):
                continue

            if isValid(s, target):
                longeststring = target
        return longeststring

