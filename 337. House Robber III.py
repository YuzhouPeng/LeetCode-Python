# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root==None:
                return [0,0]
            robLeft = dfs(root.left)
            robRight = dfs(root.right)
            norobCur = robLeft[1]+robRight[1]
            robCur = max(robLeft[0]+robRight[0]+root.val,norobCur)
            return [norobCur,robCur]
        return dfs(root)[1]