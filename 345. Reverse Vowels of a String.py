class Solution(object):
    def reverseVowels(self,s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        i = 0
        j = len(s)-1
        result =  [None]*len(s)
        while i<=j:
            chari = s[i]
            charj = s[j]
            if chari not in vowels:
                result[i] = chari
                i = i+1
            elif charj not in vowels:
                result[j] = charj
                j = j-1
            else:
                result[i] = charj
                result[j] = chari
                i = i+1
                j = j-1
        return ''.join(result)


