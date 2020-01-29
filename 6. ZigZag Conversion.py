class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or len(s)<numRows:
            return s
        #L里面的每个“”代表的是输出矩阵每行的字符串 长度为numRows
        L = ['']*len(s)
        step = 1
        index = 0
        #按顺序把字符串每个字符分配到输出的每一行中
        for x in s:
            L[index]+=x
            if index==0:
                step = 1
            elif index == numRows-1:
                step = -1
            index+=step
        return "".join(L)