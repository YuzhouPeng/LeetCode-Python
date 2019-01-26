# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def iterate(self, root, counter):
        if root == None:
            return
        counter[root.val] += 1
        self.iterate(root.left, counter)
        self.iterate(root.right, counter)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = collections.Counter()

        if root == None:
            return []
        self.iterate(root, counter)
        # maxvalue = max(counter.values())
        # return [e for e, v in enumerate(counter) if v == maxvalue]
        max_freq = max([freq for node, freq in counter.most_common()])
        return [node for node, freq in counter.most_common() if freq == max_freq]

