# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        stk=[]
        root=TreeNode(preorder[0])
        stk.append(root)
        for i in range(1,len(preorder)):
            node=TreeNode(preorder[i])
            if node.val<stk[-1].val:
                stk[-1].left=node
                stk.append(node)
            else:
                last=None
                while stk and stk[-1].val<node.val:
                    last=stk.pop()
                last.right=node
                stk.append(node)
        return root

        