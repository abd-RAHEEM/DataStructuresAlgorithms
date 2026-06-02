# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph={}
        def build_graph(node, parent=None):
            if not node:
                return
            if node.val not in graph:
                graph[node.val]=[]
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left,node)
            build_graph(node.right,node)
        build_graph(root)
        queue=deque([(target.val,0)])
        result=[]
        visited={target.val}
        while queue:
            curr_val,dist=queue.popleft()
            if dist==k:
                result.append(curr_val)
            elif dist<k:
                for neighbor in graph[curr_val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,dist+1))
        return result

        