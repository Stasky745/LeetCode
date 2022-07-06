import time

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # If numRows = 3
        # L = [[], [], []]
        # Each one for a row
        L = [[] for _ in range(numRows)]
        index, step = 0, 1

        for x in s:
            # We add the character to the specific row
            L[index].append(x)
            
            # If we are on index 0 (decreasing), we put positive step (increasing)
            if index == 0:
                step = 1
            
            # If we reach numRows (increasing), we put negative step (decreasing)
            elif index == numRows -1:
                step = -1
            index += step

        # We join everything into a single string
        return ''.join(''.join(row) for row in L)
                    
                    


# Program
s1 = "PAYPALISHIRING"
n1 = 3
s2 = "PAYPALISHIRING"
n2 = 4
s3 = "A"
n3 = 1
s4 = "ABCD"
n4 = 3

t0 = time.perf_counter_ns()

s = Solution()

print(s.convert(s1, n1))
print(s.convert(s2, n2))
print(s.convert(s3, n3))
print(s.convert(s4, n4))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
