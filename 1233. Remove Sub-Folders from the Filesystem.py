class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        ans = []
        for f in folder:
            if not ans or f[:1+len(ans[-1])]!=ans[-1]+"/":
                ans.append(f)
        return ans