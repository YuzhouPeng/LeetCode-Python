# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def issymmetric(t1,t2):
    if t1==None and t2==None:
        return True
    if t1==None or t2==None:
        return False
    if t1.val!=t2.val:
        return False
    return issymmetric(t1.left,t2.right) and issymmetric(t1.right,t2.left)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return issymmetric(root.left,root.right)
