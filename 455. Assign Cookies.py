class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        list.sort(g)
        list.sort(s)
        i=0
        j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i = i+1
            j = j+1

        return i