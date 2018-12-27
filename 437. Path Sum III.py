# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def pathsumwithroot(root,sum):
    if root==None:
        return 0
    ret = 0
    if root.val==sum:
        ret+=1
    ret+=pathsumwithroot(root.left,sum-root.val)+pathsumwithroot(root.right,sum-root.val)

    return ret
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root==None:
            return 0
        ret = pathsumwithroot(root,sum)+ self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        return ret