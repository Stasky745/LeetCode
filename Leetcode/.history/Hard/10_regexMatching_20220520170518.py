import time

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # We will create a 2D Matrix
        rows = len(s)
        columns = len(p)            
        
        # Base conditions
        
        
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