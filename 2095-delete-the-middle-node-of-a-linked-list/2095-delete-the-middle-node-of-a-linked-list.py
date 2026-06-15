# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :type rtype: Optional[ListNode]
        """
        # Edge Case: If the list has only 1 node, deleting it leaves the list empty.
        if not head or not head.next:
            return None
        
        # Initialize slow at the head, and fast two steps ahead
        slow = head
        fast = head.next.next
        
        # Move fast by 2 steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is now right before the middle node. Skip the middle node.
        slow.next = slow.next.next
        
        return head