import time

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # base cases
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
            
        max_len = 1     # Length of the palindrome
        start = 0       # 1st character of the palindrome
        
        
        for i in range(len(s)):
            ## odd palindromes
            if (
                i - max_len >= 1                                                    # i has space to create a palindrome bigger than max_length (max_length isn't out of bounds of current i)
                and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]      # substring with i at center and max_len to each side are equal to each other
            ):
                start = i - max_len - 1
                max_len += 2
                continue
            
            ## even palindromes
            if (
                i - max_len >= 0                                                    # i has space to create a palindrome bigger than max_length (max_length isn't out of bounds of current i)
                and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]              # substring with i at center and max_len to each side are equal to each other
            ):
                start = i - max_len
                max_len += 1
                
        return s[start:start + max_len]


# Program
s1 = "babad"
s2 = "cbbd"

t0 = time.perf_counter_ns()

s = Solution()

print(s.longestPalindrome(s1))
print(s.longestPalindrome(s2))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
