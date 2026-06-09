# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.results=-1
        self.arr=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)
        inorder(root)
        k=1
        self.arr.sort()
        i=0
        k=1
        while i<len(self.arr)-1:
            if self.arr[i]!=self.arr[i+1]:
                k+=1
                self.results=self.arr[i+1]
                return self.results
            i+=1
        return self.results 

        