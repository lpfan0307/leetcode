# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        p = headA
        while p:
            lenA += 1
            p = p.next
        p = headB
        while p:
            lenB += 1
            p = p.next
        if lenA < lenB:
            p = headA
            headA = headB
            headB = p
        num = lenB - lenA
        if lenA > lenB:
            num = lenA - lenB
        
        for i in range(num):
            headA = headA.next
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None