# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :param l1:
        :param l2:
        :return:
        """
        result = ListNode(0)
        head = result
        carry_bit = 0
        while l1 is not None and l2 is not None:
            s = l1.val+l2.val +carry_bit
            v = s%10
            carry_bit = 1 if s>=10 else 0
            node = ListNode(v)
            result.next = node
            result = node
            l1 = l1.next
            l2 = l2.next
        if l1 is not None:
            l2 = l1
        while l2 is not None:
            s = l2.val + carry_bit
            v = s%10
            carry_bit = 1 if s>=10 else 0
            node = ListNode(v)
            result.next = node
            result = node
            l2 = l2.next
        if carry_bit==1:
            node = ListNode(1)
            result.next = node
        head = head.next
        return head
