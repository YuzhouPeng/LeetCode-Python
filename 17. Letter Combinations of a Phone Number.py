KEYS = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
def doCombinations(prefix,combinations,digits):
    test = digits[0]
    if len(prefix)==len(digits):
        combinations.append(''.join(prefix))
        return
    curdigits = int(digits[len(prefix)])
    letters = KEYS[curdigits]
    for c in letters:
        prefix.append(c)
        doCombinations(prefix,combinations,digits)
        del prefix[len(prefix)-1]
    return
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combinations = []
        if len(digits)==0 or digits==None:
            return combinations
        prefix = []
        doCombinations(prefix,combinations,digits)
        return combinations


