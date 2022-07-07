import time
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        res = 0
        
        while left < right:
            if height[left] < height[right]:
                res = height[left] * (right - left) if height[left] * (right - left) > res else res
                left += 1
            else:
                res = height[right] * (right - left) if height[right] * (right - left) > res else res
                right -= 1
                
        return res
        
                    
                    


# Program
x1 = [1,8,6,2,5,4,8,3,7]
x2 = [1,1]

t0 = time.perf_counter_ns()

s = Solution()

print(s.maxArea(x1))
print(s.maxArea(x2))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
