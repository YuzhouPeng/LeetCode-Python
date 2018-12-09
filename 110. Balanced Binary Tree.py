# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxDepth(self,root):
        global result
        if root == None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if abs(l-r)>1:
            result = False
        return 1+max(l,r)
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        global result
        result = True
        self.maxDepth(root)
        return result