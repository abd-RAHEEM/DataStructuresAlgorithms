# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node,cur):
            if not node:
                return 0
            cur=cur*10+node.val
            if not node.left and not node.right:
                return cur
            return dfs(node.left,cur)+dfs(node.right,cur)
        return dfs(root,0)