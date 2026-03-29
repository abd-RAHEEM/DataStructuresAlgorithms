# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        queue=deque([root])
        left_right=True
        res=[]
        while queue:
            level=[]
            for _ in range(len(queue)):
                
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_right:
                level=level[::-1]
            res.append(level)
            left_right= not left_right
        return res
        