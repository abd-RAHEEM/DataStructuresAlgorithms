# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        def dfs(L,R):
            if not L and not R:
                return True
            if not L or not R:
                return False
            return (L.val==R.val) and dfs(L.left,R.right) and dfs(L.right,R.left)
        return dfs(root.left,root.right)            