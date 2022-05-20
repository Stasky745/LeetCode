# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

import math
import time
from typing import List

class Solution(object):
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        steps = 1
        log = math.log(num, 2)
        while not log.is_integer():
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2

            log = math.log(num, 2)
            steps += 1

        steps += int(log)

        return steps

        


s = Solution()


# Program
t0 = time.perf_counter_ns()

print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))
print(s.numberOfSteps(0))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")