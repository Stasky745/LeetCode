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
        
        for i in range(0, max(len(l1), len(l2))):
            if i < len(l1):
                l1_digit = l1[i]
            else:
                l1_digit = 0
                
            if i < len(l2):
                l2_digit = l2[i]
            else:
                l2_digit = 0
                
            sum = l1_digit + l2_digit + rest
            
            result += sum % 10 * 10 ^ i
            rest = int(sum/10)
            
        return result
    
# Program
l1 = [2,4,3]
l2 = [5,6,4]

t0 = time.perf_counter_ns()

s = Solution()

print(s.addTwoNumbers(l1, l2))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    