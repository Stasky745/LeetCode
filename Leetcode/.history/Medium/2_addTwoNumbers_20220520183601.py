import time
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        last = ListNode(-1)
        node = last
        
        while l1 and l2:
            # We calculate the sum            
            sum = l1.val + l2.val + carry
            
            # We create the new node, append it and update last to point to it
            last.next = ListNode(sum % 10, None)
            last = last.next                
                
            # We update the carry
            carry = int(sum/10)
            
            # We update l1 and l2
            l1 = l1.next
            l2 = l2.next
        
        # If there are still nodes in l1
        while l1:
            # We calculate the sum            
            sum = l1.val + carry
            
            # We create the new node, append it and update last to point to it
            last.next = ListNode(sum % 10, None)
            last = last.next
            
            # We update the carry
            carry = int(sum/10)
            
            # We update l1
            l1 = l1.next
            
        # If there are still nodes in l2
        while l2:
            # We calculate the sum            
            sum = l2.val + carry
            
            # We create the new node, append it and update last to point to it
            last.next = ListNode(sum % 10, None)
            last = last.next
            
            # We update the carry
            carry = int(sum/10)
            
            # We update l2
            l2 = l2.next
            
        # If there's remaining carry we update it
        while carry > 0:
            # We calculate the sum            
            sum = carry
            
            # We create the new node, append it and update last to point to it
            last.next = ListNode(sum % 10, None)
            last = last.next
            
            # We update the carry
            carry = int(sum/10)
            
        return node
    
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