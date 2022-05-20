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
        
        # empty string and empty pattern are a match
        matrix[0][0] = True
        
        # Deals with *
        for i in range(2, columns + 1):
            if p[i-1] == '*':
                matrix[0][i] == matrix[0][i-2]
                
        # Rest of characters
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    matrix[i][j] = matrix[i-1][j-1]
                elif j > 1 and p[j-1] == '*':
                    matrix[i][j] = matrix[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        matrix[i][j] = matrix[i][j] or matrix[i-1][j]
        
        return matrix[rows][columns]
    
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