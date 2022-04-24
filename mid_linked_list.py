import time
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
        
node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
node2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

# Program
t0 = time.perf_counter_ns()

s = Solution()

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")