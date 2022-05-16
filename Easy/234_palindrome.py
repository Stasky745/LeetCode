import time
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # We revert a ListNode until we find a None
        def reverse(node):
            prev = None
            curr = node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        # We compare ListNodes     
        def areEqual(node1, node2):
            while node1 and node2:
                # If the value is different it's false
                if node1.val != node2.val:
                    return False
                node1 = node1.next
                node2 = node2.next

            # If both are None they were the same
            return not (node1 or node2)
        
        # Only 1 element
        if not head.next:
            return True

        prev = None
        slow = fast = head
        
        # We try to find halfway head (slow will be half when fast finishes)
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Consider if the list has even or odd number of elements
        if fast:
            slow = slow.next

        # Prev is a node inside head, if we put prev.next to None, we get a None inside head that marks halfway the list
        if prev:
            prev.next = None
        head = reverse(head)
        return areEqual(head, slow)


# Program
ln1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
ln2 = ListNode(1, ListNode(2, None))

t0 = time.perf_counter_ns()

s = Solution()

print(s.isPalindrome(ln1))
print(s.isPalindrome(ln2))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")