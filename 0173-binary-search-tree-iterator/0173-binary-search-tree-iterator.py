# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stk=[]
        cur=root
        self.stk.append(cur)
        while cur.left:
            self.stk.append(cur.left)
            cur=cur.left
        

    def next(self):
        """
        :rtype: int
        """

        popped=self.stk.pop()
        cur=popped
        if cur.right:
            self.stk.append(cur.right)
            cur=cur.right
            while cur.left:
                self.stk.append(cur.left)
                cur=cur.left
        return popped.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk)!=0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()