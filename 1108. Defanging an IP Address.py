class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ""
        for a in address:
            if a=='.':
                res+="[.]"
            else:
                res+=a
        return res