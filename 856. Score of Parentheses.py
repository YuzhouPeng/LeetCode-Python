class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for x in S:
            if x == "(":
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] = max(2*v,1)
        return stack.pop()