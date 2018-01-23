class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s))%2==1:
            return False
        i=0
        flag = 0
        while s[i] != None:
            if s[i]=='(' & s[i+1]!=')':
                return False
            if s[i]=='{' & s[i+1]!='}':
                return False
            if s[i]=='[' & s[i+1]!=']':
                return False
            i=i+1
        return True