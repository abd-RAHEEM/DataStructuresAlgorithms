# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque
        queue=deque([(root,0)])
        max_width=0
        while queue:
            level_length=len(queue)
            _,first_index=queue[0]
            for i in range(level_length):
                node,index=queue.popleft()
                if i==level_length-1:
                    width=index-first_index+1
                    max_width=max(max_width,width)
                if node.left:
                    queue.append((node.left,2*index))
                if node.right:
                    queue.append((node.right,2*index+1))
        return max_width


        