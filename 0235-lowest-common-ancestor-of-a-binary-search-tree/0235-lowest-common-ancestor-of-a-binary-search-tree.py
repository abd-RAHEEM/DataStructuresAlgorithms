# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node.val > p.val and node.val>q.val:
                return dfs(node.left)
            elif node.val <p.val and node.val<q.val:
                return dfs(node.right)
            else:
                return node
        return dfs(root)
        