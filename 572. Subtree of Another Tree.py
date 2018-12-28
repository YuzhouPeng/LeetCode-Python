# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def issubtreewithroot(s,t):
    if t==None and s==None:
        return True
    if t==None or s==None:
        return False
    if s.val!=t.val:
        return False
    return issubtreewithroot(s.left,t.left) and issubtreewithroot(s.right,t.right)
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s==None:
            return False
        return issubtreewithroot(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)