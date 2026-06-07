# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        curr=root
        while curr:
            if curr.left:
                predecessor=curr.left
                while predecessor.right:
                    predecessor=predecessor.right
                predecessor.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right
        
