# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.postorder_idx=len(postorder)-1
        inorder_map={val:i for i,val in enumerate(inorder)}
        def arr_tree(left,right):
            if left>right or self.postorder_idx<0:
                return None
            root_val=postorder[self.postorder_idx]
            self.postorder_idx-=1
            root=TreeNode(root_val)
            inorder_idx=inorder_map[root_val]
            root.right=arr_tree(inorder_idx+1, right)
            root.left=arr_tree(left,inorder_idx-1)
            

            return root
        return arr_tree(0,len(inorder)-1)