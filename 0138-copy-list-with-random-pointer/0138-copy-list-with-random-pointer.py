"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old_to_new={}
        if not head:
            return None
        cur=head
        while cur:
            old_to_new[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy_node=old_to_new.get(cur)
            copy_node.next=old_to_new.get(cur.next)
            copy_node.random=old_to_new.get(cur.random)
            cur=cur.next
        return old_to_new[head]
