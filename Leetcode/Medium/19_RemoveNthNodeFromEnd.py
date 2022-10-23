# Definition for singly-linked list.
from typing import Optional
from modules.listNode import ListNode
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        nNodes, nSlow = 1, 1

        # Get the number of nodes
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            nSlow += 1

        if fast:
            nNodes = nSlow * 2 - 1
        else:
            nNodes = nSlow * 2 - 2

        # Skip the head if it's number of nodes
        if n == nNodes:
            return head.next

        
        # Find the node we have to delete
        nDelete = nNodes + 1 - n


        # If we've passed the node we have to delete, we start counting from the start
        if nDelete <= nSlow:
            slow = head
            nSlow = 1

        while nSlow < nDelete - 1:
            slow = slow.next
            nSlow += 1
        
        if not slow.next:
            return None
        
        slow.next = slow.next.next

        return head



    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        nNodes, nSlow = 1, 1
        nodeDict = {}

        # Get the number of nodes while storing the node with its index in our dict
        while fast and fast.next:
            nodeDict[nSlow] = slow

            fast = fast.next.next
            slow = slow.next

            nSlow += 1

        if fast:
            nNodes = nSlow * 2 - 1
        else:
            nNodes = nSlow * 2 - 2

        # Skip the head if it's number of nodes
        if n == nNodes:
            return head.next


        # Find the node we have to delete
        nDelete = nNodes + 1 - n


        # If the node we have to delete is one prior to the one we're at, we have it in the dict
        if nDelete - 1 in nodeDict:
            nodeBeforeDelete = nodeDict[nDelete - 1]

            if not nodeBeforeDelete.next:
                return None

            nodeBeforeDelete.next = nodeBeforeDelete.next.next
            return head
        else:
            while nSlow < nDelete - 1:
                slow = slow.next
                nSlow += 1
            
            if not slow.next:
                return None
            
            slow.next = slow.next.next

            return head

        

s = Solution()

l = ListNode([1,2])

r = s.removeNthFromEnd2(l, 1)

r.print()