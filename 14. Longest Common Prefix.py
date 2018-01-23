class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        prefixString = strs[0]
        for i in range(len(strs[0])):
            for str1 in strs[1:]:
                if i >= len(str1) or str1[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

