# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        def getHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            # Left subtree is perfect
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect but smaller
            return (1 << right_height) + self.countNodes(root.left)

        