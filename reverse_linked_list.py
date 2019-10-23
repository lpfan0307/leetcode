class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        q = ListNode(head.val)
        p = head.next
        while p is not None:
            node = ListNode(p.val)
            node.next = q
            q = node
            p = p.next
        return q
