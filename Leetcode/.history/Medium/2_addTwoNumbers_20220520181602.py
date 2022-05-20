import time
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = 0
        result = 0
        i = 0
        node = None
        
        while l1 or l2:
            if l1:
                l1_digit = l1.val
            else:
                l1_digit = 0
                
            if l2:
                l2_digit = l2.val
            else:
                l2_digit = 0
                
            sum = l1_digit + l2_digit + rest
            
            node = ListNode(sum % 10, node)
            rest = int(sum/10)
            
            i += 1
            l1 = l1.next
            l2 = l2.next
            
        return result
    
# Program
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))

t0 = time.perf_counter_ns()

s = Solution()

print(s.addTwoNumbers(l1, l2))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    