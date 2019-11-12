class Solution:
    def copyRandomList(self, head):
            if not head:
                return None
            copyHead = Node(head.val,None,None)
            #hash to associate the id of every original node to the respective copy
            hsh = {id(head): copyHead}

            #First pass copies values and next
            curr = head
            copyCurr = copyHead
            while curr:
                if curr.next:
                    copyCurr.next = Node(curr.next.val,None,None)
                    hsh[id(curr.next)] = copyCurr.next
                curr = curr.next
                copyCurr = copyCurr.next

            #second pass copies random
            curr = head
            copyCurr = copyHead
            while curr:
                if curr.random:
                    copyCurr.random = hsh[id(curr.random)]
                else:
                    copyCurr.random = None
                curr = curr.next
                copyCurr = copyCurr.next
            return copyHead