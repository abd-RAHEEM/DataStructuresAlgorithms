# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        cur=root
        while cur:
            if cur.val>val:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=TreeNode(val)
                    return root
            else:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=TreeNode(val)
                    return root
    