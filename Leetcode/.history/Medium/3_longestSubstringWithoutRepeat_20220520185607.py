import time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        
        for i in range(len(s)):
            char = s[i]
            seen = []
            aux = 1
            while char not in seen:
                seen.append(char)
                char = s[i + aux] if i+aux < len(s) else char
                aux += 1
            
            if length < len(seen):
                length = len(seen)
            
        return length
    
# Program
s1 = "abcabcbb"
s2 = "bbbbbbbb"
s3 = "pwwkew"

t0 = time.perf_counter_ns()

s = Solution()

print(s.lengthOfLongestSubstring(s1))
print(s.lengthOfLongestSubstring(s2))
print(s.lengthOfLongestSubstring(s3))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    