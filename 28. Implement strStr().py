class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        flag = 0
        haystackLen = len(haystack)
        needleLen = len(needle)
        if haystackLen == 0 and needleLen == 0:
            return 0
        if needleLen == 0:
            return 0
        if haystackLen == 0:
            return -1
        if haystackLen < needleLen:
            return -1
        for i in range(haystackLen):
            if haystack[i] == needle[0] and haystackLen-i >= needleLen:
                for j in range(needleLen):
                    if (i+j) < haystackLen and haystack[i+j] == needle[j]:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    return i
        return -1