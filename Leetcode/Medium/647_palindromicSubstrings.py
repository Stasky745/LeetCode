import time

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        def pal(s, left, right):
            count = 0
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
            return count
        
        for i in range(len(s)):
            result += pal(s, i, i)       # odd palindromes
            result += pal(s, i, i+1)     # even palindromes

        
        return result


# Program
s1 = "abc"
s2 = "aaa"

t0 = time.perf_counter_ns()

s = Solution()

print(s.countSubstrings(s1))
print(s.countSubstrings(s2))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
