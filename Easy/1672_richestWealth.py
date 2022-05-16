# https://leetcode.com/problems/richest-customer-wealth/

import math
import time
from typing import List

class Solution(object):
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for customer in accounts:
            total = sum(customer)
            if total > max:
                max = total

        return max

        


s = Solution()


# Program
t0 = time.perf_counter_ns()

print(s.maximumWealth([[1,2,3],[3,2,1]]))
print(s.maximumWealth([[1,5],[7,3],[3,5]]))
print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")