# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stk=[]
        depth=0
        cur=1
        if root:
            stk.append((root,cur))
        while stk:
            node,cur=stk.pop()
            depth=max(depth,cur)
            if node.left:
                stk.append((node.left,cur+1))
            if node.right:
                stk.append((node.right,cur+1))
            
        return depth       

        