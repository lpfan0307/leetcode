class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(None)
        l = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            l.next = node
            l = l.next
        if l1 is None:
            l1 = l2
        while l1 is not None:
            node = ListNode(l1.val)
            l.next = node
            l = l.next
            l1 = l1.next
        head = head.next
        return head
