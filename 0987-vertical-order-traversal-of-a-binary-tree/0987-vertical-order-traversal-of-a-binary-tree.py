# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes=[]
        def dfs(node,row,col):
         if not node:
             return 
         nodes.append((col,row,node.val))
         dfs(node.left,row+1,col-1)
         dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        nodes.sort(key=lambda x: (x[0],x[1],x[2]))
        res=defaultdict(list)
        for col,row,val in nodes:
         res[col].append(val)
        return [res[c] for c in sorted(res.keys())]