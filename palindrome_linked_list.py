# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        origin_head = head
        while head is not None:
            l.append(head.val)
            head = head.next
        head = origin_head
        while head is not None:
            if head.val != l.pop():
                return False
            head = head.next
        return True