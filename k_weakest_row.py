# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import time
from typing import List

class Solution(object):
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict = {}
        n_row = 0
        for row in mat:
            n_soldiers = 0
            i = 0
            while i < len(row) and row[i] == 1:
                n_soldiers += 1
                i += 1
            
            dict[n_row] = n_soldiers

            n_row += 1
        
        result = sorted(dict, key=dict.get)

        return result[0:k]

        
        
mat1 = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]

mat2 = [
    [1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]
]
s = Solution()


# Program
t0 = time.perf_counter_ns()

print(s.kWeakestRows(mat1, 3))
print(s.kWeakestRows(mat2, 2))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")