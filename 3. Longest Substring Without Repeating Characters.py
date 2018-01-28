class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(s)
        set1 = set()
        if s == "":
            return 0
        MaxLength = 0
        Location = {}
        index = -1
        for i in range(strLen):
            if Location.get(s[i]) > index:
                index = Location.get(s[i])
            if i - index > MaxLength:
                MaxLength = i- index
            Location[s[i]] = i
        return MaxLength
