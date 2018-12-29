# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return -1
        if root.left==None and root.right==None:
            return -1
        leftval = root.left.val
        rightval = root.right.val
