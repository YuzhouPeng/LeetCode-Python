# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if root == None:
            return res
        q = [root]
        while q:
            q1 = []
            total = 0
            cnt = 0
            while q:
                node = q.pop()
                if node.left!=None:
                    q1.append(node.left)
                if node.right!=None:
                    q1.append(node.right)
                total+=node.val
                cnt+=1
            res.append(total*1.0/cnt)
            q = list(q1)
        return res