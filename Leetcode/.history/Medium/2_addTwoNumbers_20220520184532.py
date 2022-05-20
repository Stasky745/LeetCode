import time
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        last = node = ListNode(-1)
        
        while l1 or l2:
            # We get the value of both lists
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
                
            # We get the total of the sum
            sum = v1 + v2 + carry
            
            # create the new node and update last
            last.next = ListNode(sum % 10, None)
            last = last.next
                
            # update to new carry
            carry = sum//10
            
            # update lists to the next value
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # add any remaining carry
        if carry:
            last.next = ListNode(carry, None)
            
        return node.next
    
# Program
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))

r1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
r2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

t0 = time.perf_counter_ns()

s = Solution()

print(s.addTwoNumbers(l1, l2))
print(s.addTwoNumbers(r1, r2))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    