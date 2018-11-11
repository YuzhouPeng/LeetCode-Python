def ispalimndrome(s, p1, p2):
    while (p1 < p2):
        if (s[p1] != s[p2]):
            return False
        p1 = p1 + 1
        p2 = p2 - 1
    return True
class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return ispalimndrome(s,i,j-1) or ispalimndrome(s,i+1,j)
            i = i+1
            j = j-1
        return True
