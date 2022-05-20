from ast import pattern
import time

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # We will create a 2D Matrix
        rows = len(s)
        columns = len(p)            
        
        # Base conditions
        if rows == 0 and columns == 0:
            return True
        if columns == 0:
            return False
        if p == "*":
            return True
        
        # We create the matrix (+1 to size to account if one or both strings are empty)
        matrix = [[False for j in range(columns + 1)] for i in range(rows + 1)]
        
        return True
    
# Program
s1 = "aa"
p1 = "a"

s2 = "aa"
p2 = "a*"

s3 = "ab"
p3 = ".*"

t0 = time.perf_counter_ns()

s = Solution()

print(s.isMatch(s1, p1))
print(s.isMatch(s2, p2))
print(s.isMatch(s3, p3))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    