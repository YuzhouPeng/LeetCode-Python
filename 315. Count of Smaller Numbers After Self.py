class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum)/2
            if half:
                left,right = sort(enum[:half]),sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not left or right and left[-1][1]>right[-1][1]:
                        result[left[-1][0]]+=len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        result = [0]*len(nums)
        enums = sort(list(enumerate(nums)))
        return result