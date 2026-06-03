# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.preorder_idx=0
        inorder_map={val:i for i, val in enumerate(inorder)}

        def graph_to_tree(left,right):
            if left>right:
                return None
            root_val=preorder[self.preorder_idx]

            root=TreeNode(root_val)
            inorder_idx=inorder_map[root_val]
            self.preorder_idx+=1
            root.left=graph_to_tree(left, inorder_idx-1)
            root.right=graph_to_tree(inorder_idx+1,right)
            return root

        return graph_to_tree(0, len(inorder)-1)

