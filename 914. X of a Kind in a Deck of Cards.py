import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck)<=1:
            return False
        values = []
        counter = collections.Counter(deck)
        for k in counter.keys():
            values.append(counter[k])
        if hcf(values)==1:
            return False
        return True
def hcf(x):                                #计算最大公约数
    smaller=min(x)
    for i in reversed(range(1,smaller+1)):
        if list(filter(lambda j: j%i!=0,x)) == []:
            return i

