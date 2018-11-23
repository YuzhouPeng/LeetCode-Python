# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def buildPath(values):
    str1 = []
    for i in range(len(values)):
        str1.append(str(values[i]))
        if (i!=len(values)-1):
            str1.append('->')
    return ''.join(str1)

def isLeaf(node):
    return node.left==None and node.right==None

def backtracking(node,values,paths):
    if node==None:
        return
    values.append(node.val)
    if isLeaf(node):
        paths.append(buildPath(values))
    else:
        backtracking(node.left, values, paths)
        backtracking(node.right, values, paths)
    del values[len(values)-1]


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if root == None:
            return paths
        values = []
        backtracking(root, values, paths)
        return paths