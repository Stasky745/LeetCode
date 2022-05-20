import time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # Start from the beginning of the string
        # See if the current visiting letter has already been visited or not. 
        # If it has been visited previously then its a duplicate. To make sure we are marking the most recent letter, we store only the index of the most recent letter for the duplicates letter in the seen.
        # If you encounter a duplicate but your current left position is greater than the duplicate index then ignore it. and update the index of the duplicate letter. Else start from the right of the previous index of duplicate 
        # Every time, you don't see any duplicates, compute the max and check with the current max.
        # Return the max computed
        '''
        
        
        # Map with position of the characters {char: position}
        used = {}
        
        # Start variable is where we start counting
        max_length = start = 0
        
        for i, c in enumerate(s):
            # If we have seen 'c' but the last time we updated start was on a past iteration, we update start
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            used[c] = i

        
        return max_length
    
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