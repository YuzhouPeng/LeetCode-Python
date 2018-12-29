# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
pathvalue=0



class Solution:
    def dfs(self,root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        leftvalue = 0
        rightvalue = 0
        if root.left != None and root.left.val == root.val:
            leftvalue = left + 1

        if root.right != None and root.right.val == root.val:
            rightvalue = right + 1


        self.res = max(self.res, leftvalue + rightvalue)
        return max(leftvalue, rightvalue)
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
