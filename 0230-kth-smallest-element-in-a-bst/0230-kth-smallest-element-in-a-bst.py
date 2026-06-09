class Solution(object):
    def kthSmallest(self, root, k):
        self.key = 0
        self.result = None

        def inor(node):

            if not node or self.result is not None:
                return

            inor(node.left)

            self.key += 1
            if self.key == k:
                self.result = node.val
                return

            inor(node.right)

        inor(root)
        return self.result
        