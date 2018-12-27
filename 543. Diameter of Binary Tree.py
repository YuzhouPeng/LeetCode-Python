# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self,root):
        if root==None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.ans = max(self.ans,left+right)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        self.traverse(root)
        return self.ans
