import time
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        return -1
    
# Program
grid1 = [[0,1],[1,0]]

t0 = time.perf_counter_ns()

s = Solution()

print(s.shortestPathBinaryMatrix(grid1))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    