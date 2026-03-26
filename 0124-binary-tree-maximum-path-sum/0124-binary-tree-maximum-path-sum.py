# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxx=float('-inf')
        def dfs(node):
            if not node:
                return 0
            left=max(dfs(node.left),0)
            right=max(dfs(node.right),0)
            self.maxx=max(self.maxx,left+node.val+right)
            return node.val +max(left,right)
        dfs(root)
        return self.maxx
        