class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        numlist = []
        while num>0:
            numlist.append(num%10)
            num/=10
        numlist = numlist[::-1]
        # print(numlist)
        flag = 0
        result = 0
        for n in numlist:
            result*=10
            if n==6 and flag==0:
                result+=9
                flag=1
            else:
                result+=n
        print(result)
        return result